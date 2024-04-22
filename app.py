from flask import Flask, render_template

app = Flask(__name__)

# Route to render the HTML template
@app.route('/')
def index():
     # Replace this value with the percentage you want to display
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

























'''from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/static/css/<path:filename>')
def serve_static(filename):
  return app.send_static_file(f'css/{filename}') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    gene_data = {}  # Dictionary to store gene inputs
    for i in range(1, 11):  # Loop through input fields for genes 1 to 10
        gene_name = f'gene{i}'
        gene_input = request.form.get(gene_name)
        gene_hidden = request.form.get(f'{gene_name}_hidden')
        gene_data[gene_name] = {'input': gene_input, 'hidden': gene_hidden}
    
    # Render the result template with the received data
    return render_template('results.html', gene_data=gene_data)

if __name__ == '__main__':
    app.run(debug=True)'''