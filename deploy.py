#!/usr/bin/env python3
import os
import subprocess
import sys
import logging
import logging.handlers
import pathlib

def setup_logging():
    """Setup logging - gör detta FÖRST i main()"""
    # Create logs
    pathlib.Path('logs').mkdir(exist_ok=True)
    
    # Konfigurera logging med file rotation
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)8s] %(name)s: %(message)s',
        handlers=[
            # File handler med rotation
            logging.handlers.RotatingFileHandler(
                'logs/app.log',
                maxBytes=10*1024*1024,  # 10MB per fil
                backupCount=5,          # Behåll 5 gamla filer
                encoding='utf-8'
            ),
            # Console handler
            logging.StreamHandler()
        ]
    )
    
    # Returnera en logger för main-modulen
    return logging.getLogger(__name__)

logger = setup_logging()

def main() -> int:
    # 1
    logger.info('Started main')
    done = False
    while not done:
        try:
            ip_address = input('Enter IP address for VM (ansible_host; hostname -I | awk "{print $1}" in ubuntu vm):')
            username = input('Enter ubuntu user for SSH (ansible_user; whoami in ubuntu vm | echo $USER):')
            return 0
            1/0

        
        except Exception as e:
            logger.critical(f'Exception was thrown: {e}')
            return 1


if __name__ == '__main__':
    exit_code = main()

    print(f'exit_code= {exit_code}\n sys.exit({exit_code})')
    if exit_code == 0:
        logger.info('Successfully executed')
        sys.exit(exit_code)
    else:
        logger.error('Unsuccessfully executed')
        sys.exit(exit_code)