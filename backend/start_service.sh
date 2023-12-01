
echo "Establishing environment variables..."
python export HUGGINGFACEHUB_API_TOKEN=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

# Start service
echo "Starting service..."
python manage.py runserver 0.0.0.0:5000