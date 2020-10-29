from application import app

#region the driver method
if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
#endregion  
