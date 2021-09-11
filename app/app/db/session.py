import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if os.environ.get('DEPLOY_ENV') == 'TEST':
    logger.info('数据库连接到单元测试')
    engine = create_engine('sqlite:///test.db', pool_pre_ping=True)
else:
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
