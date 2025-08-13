#!/bin/bash

set -e  # Exit on any error

# Check if we're in a virtual environment
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "❌ Error: This script must be run from within a virtual environment!"
    echo ""
    echo "Please run the following commands first:"
    echo "   python3 -m venv venv"
    echo "   source venv/bin/activate"
    echo "   ./setup-dev.sh"
    echo ""
    exit 1
fi

echo "✅ Virtual environment detected: $VIRTUAL_ENV"
echo "🚀 Starting TDD Labs development environment setup..."

# Check if Python 3.8+ is installed
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | cut -d' ' -f2)
required_version="3.8"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" 2>/dev/null; then
    echo "❌ Error: Python 3.8+ is required. Found: $python_version"
    exit 1
fi
echo "✅ Python version: $python_version"

# Since we're already in a virtual environment, skip venv creation/activation

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install the package in development mode with all dependencies
echo "📦 Installing tdd-labs with all dependencies (dev + test)..."
pip install -e ".[dev,test]"

echo ""
echo "🎉 Installation completed successfully!"
echo ""
echo "📋 Available commands:"
echo "   • Run tests: pytest"
echo "   • Format code: black ."
echo "   • Check types: mypy ."
echo "   • Lint code: flake8 ."
echo ""
echo "💡 All development and testing tools are now ready!"