from aims_ui import app

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=app.config.get('UI_EXPOSED_PORT'), debug=0)
