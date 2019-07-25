from flask import Flask, request, send_from_directory, url_for, redirect
from flask import jsonify, json, copy_current_request_context
#from flask_cors import CORS, cross_origin

application = Flask(__name__,static_folder='',template_folder='')
app = application
#CORS(app)

from werkzeug.utils import secure_filename

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt','csv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#----------------------------------------------------
@app.route('/')
def index():
    return send_from_directory("./", "index.html")

@app.route('/uploadCSV2', methods=['POST'])
#@cross_origin(origin='localhost')
def uploadCSV2():
    import pdb
    #pdb.set_trace()
    
    # check if the post request has the file part
    if 'file' not in request.files:
        print('No file part')
        #return redirect(request.url)
    else:
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            #return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
        else:
            print('filetype not allowed')
            
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file', filename=filename))
        
    return jsonify({'result': 'ok!'})
    
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/test', methods=['POST','GET'])
def uploadCSVTest():

    dat = "<!doctype html>" + \
        "<title>Upload new File</title>" + \
        "<h1>Upload new File</h1>" + \
        "<form method=post enctype=multipart/form-data action=" + url_for('uploadCSV') + ">" + \
        "  <input type=file name=file>" + \
        "  <input type=submit value=Upload>" + \
        "</form>"
    return dat
    
    
@app.route('/uploadCSV', methods=['POST','GET'])
def uploadCSV():
    if True: #request.method == 'POST':
        from flask import flash
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print(file)
            
            #filename = secure_filename(file.filename)
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
 