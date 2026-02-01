#!/bin/sh

echo "======================================"
echo " Selenium Scraper Container Started"
echo " Runs every 4 hours"
echo "======================================"

while true
do
  echo "--------------------------------------"
  echo "Starting scraper at: $(date)"
  echo "--------------------------------------"

  python scrape.py
  EXIT_CODE=$?

  if [ $EXIT_CODE -ne 0 ]; then
    echo "❌ Scraper failed with exit code $EXIT_CODE"
  else
    echo "✅ Scraper completed successfully"
  fi

  echo "Sleeping for 4 hours..."
  sleep 14400   # 4 hours = 4 × 60 × 60 seconds
done
