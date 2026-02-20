from flask import Flask, render_template, request, jsonify
import sys
import io
import traceback
import re
from pyflowchart import Flowchart

app = Flask(__name__)

def improve_dsl(dsl_text):
    """
    Post-process the flowchart DSL to use correct symbols and user-friendly text.
    Creates descriptive labels that explain the logic instead of showing raw code.
    """
    lines = dsl_text.split('\n')
    improved_lines = []
    
    for line in lines:
        original_line = line
        
        # Skip empty lines and connection lines
        if not line.strip() or '->' in line or '=>' not in line:
            improved_lines.append(line)
            continue
        
        # Extract node ID and content
        if '=>' in line:
            parts = line.split('=>', 1)
            node_id = parts[0]
            rest = parts[1] if len(parts) > 1 else ''
            
            if ':' in rest:
                node_type_and_text = rest.split(':', 1)
                node_type = node_type_and_text[0].strip()
                node_text = node_type_and_text[1].strip() if len(node_type_and_text) > 1 else ''
                
                # Clean up the text based on patterns
                new_text = node_text
                
                # Handle print statements - extract what's being printed
                if 'print(' in node_text:
                    # Extract content from print()
                    match = re.search(r'print\((.*)\)', node_text)
                    if match:
                        content = match.group(1).strip()
                        # Remove quotes from string literals
                        content = re.sub(r'^["\']|["\']$', '', content)
                        new_text = f"Display: {content}"
                        node_type = 'inputoutput'
                
                # Handle input statements
                elif 'input(' in node_text:
                    # Check if it's an assignment
                    if '=' in node_text:
                        var_name = node_text.split('=')[0].strip()
                        new_text = f"Get input → {var_name}"
                    else:
                        new_text = "Get user input"
                    node_type = 'inputoutput'
                
                # Handle variable assignments (but not input)
                elif '=' in node_text and 'input(' not in node_text:
                    parts = node_text.split('=', 1)
                    var_name = parts[0].strip()
                    value = parts[1].strip() if len(parts) > 1 else ''
                    
                    # Simplify common operations
                    if '+' in value:
                        new_text = f"Add to {var_name}"
                    elif '-' in value:
                        new_text = f"Subtract from {var_name}"
                    elif '*' in value:
                        new_text = f"Multiply {var_name}"
                    elif '/' in value:
                        new_text = f"Divide {var_name}"
                    else:
                        new_text = f"Set {var_name} = {value}"
                
                # Handle for loops
                elif node_text.startswith('for ') or 'for ' in node_text:
                    match = re.search(r'for\s+(\w+)\s+in\s+(.+)', node_text)
                    if match:
                        var = match.group(1)
                        iterable = match.group(2).strip()
                        new_text = f"Loop: {var} in {iterable}"
                    else:
                        new_text = "Start loop"
                    node_type = 'operation'
                
                # Handle while loops
                elif node_text.startswith('while '):
                    condition = node_text.replace('while ', '').strip()
                    new_text = f"While {condition}?"
                    node_type = 'condition'
                
                # Handle if conditions
                elif node_text.startswith('if '):
                    condition = node_text.replace('if ', '').strip().rstrip(':')
                    new_text = f"{condition}?"
                    node_type = 'condition'
                
                # Handle function definitions
                elif node_text.startswith('def '):
                    func_name = re.search(r'def\s+(\w+)', node_text)
                    if func_name:
                        new_text = f"Function: {func_name.group(1)}"
                    node_type = 'subroutine'
                
                # Handle return statements
                elif node_text.startswith('return '):
                    value = node_text.replace('return ', '').strip()
                    new_text = f"Return {value}" if value else "Return"
                    node_type = 'operation'
                
                # Clean up function wrapper artifacts
                if 'flowchart_logic' in new_text:
                    if 'start:' in line.lower():
                        new_text = 'Start'
                        node_type = 'start'
                    elif 'end:' in line.lower():
                        new_text = 'End'
                        node_type = 'end'
                
                # Reconstruct the line
                line = f"{node_id}=>{node_type}: {new_text}"
        
        improved_lines.append(line)
    
    dsl_text = '\n'.join(improved_lines)
    
    # Add flowstate tags for styling
    dsl_text = re.sub(r'(.*=>start: .*)', r'\1|start', dsl_text)
    dsl_text = re.sub(r'(.*=>end: .*)', r'\1|end', dsl_text)
    dsl_text = re.sub(r'(.*=>operation: .*)', r'\1|operation', dsl_text)
    dsl_text = re.sub(r'(.*=>condition: .*)', r'\1|condition', dsl_text)
    dsl_text = re.sub(r'(.*=>subroutine: .*)', r'\1|subroutine', dsl_text)
    dsl_text = re.sub(r'(.*=>inputoutput: .*)', r'\1|inputoutput', dsl_text)
    
    return dsl_text

@app.route('/')
def home():
    return render_template('index.html', page='editor')

@app.route('/flowchart')
def flowchart_page():
    return render_template('flowchart.html', page='flowchart')

@app.route('/about')
def about_page():
    return render_template('about.html', page='about')

@app.route('/api/execute', methods=['POST'])
def execute_code():
    code = request.json.get('code', '')
    output_buffer = io.StringIO()
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    
    sys.stdout = output_buffer
    sys.stderr = output_buffer
    
    try:
        # Override input to prevent server hanging
        exec_globals = {
            'input': lambda prompt='': 'Input not supported in web mode'
        }
        exec(code, exec_globals)
    except Exception:
        traceback.print_exc()
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
    
    return jsonify({'output': output_buffer.getvalue()})

@app.route('/api/flowchart', methods=['POST'])
def generate_flowchart():
    code = request.json.get('code', '')
    try:
        # Try generating directly
        fc = Flowchart.from_code(code)
        flowchart_code = fc.flowchart()
        flowchart_code = improve_dsl(flowchart_code)
        return jsonify({'flowchart': flowchart_code})
    except Exception:
        # Fallback: Wrap in a function if top-level parsing fails
        try:
            wrapped_code = "def flowchart_logic():\n" + "\n".join(["    " + line for line in code.splitlines()])
            fc = Flowchart.from_code(wrapped_code)
            flowchart_code = fc.flowchart()
            flowchart_code = improve_dsl(flowchart_code)
            return jsonify({'flowchart': flowchart_code})
        except Exception as e:
            return jsonify({'error': str(e), 'flowchart': ''})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
