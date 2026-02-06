# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Component: System Setup & Environment Sync                               *
# * *
# ****************************************************************************

echo "🔧 Synchronizing environment..."

# 1. Ensure Virtual Environment exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Created new virtual environment."
fi

# 2. Activate
source venv/bin/activate

# 3. Update core tools
pip install --upgrade pip

# 4. Install from manifest
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found! Installing defaults..."
    pip install yt-dlp requests openai-whisper
fi

echo "🎉 Environment is synchronized and ready."
