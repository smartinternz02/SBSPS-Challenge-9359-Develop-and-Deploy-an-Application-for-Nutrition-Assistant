		login=True
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
		account = cursor.fetchone()
        # Show the profile page with account info
		return render_template('profile.html', account=account,login=login)
    # User is not loggedin redirect to login page
	return redirect(url_for('login'))


UPLOAD_FOLDER = 'static/uploads/'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/fitFoodie/upload',methods=['GET'])
def upload():
    return render_template('uploads.html',login=True)

@app.route('/fitFoodie/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        image = Image.open(file)
        # Get the current working directory
        cwd = os.path.dirname(os.path.abspath(__fil