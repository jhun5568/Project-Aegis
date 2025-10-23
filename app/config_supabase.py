"""
Supabase 설정 파일
WIP v0.6 - SQLite → Supabase 전환
"""

import os
import streamlit as st
from supabase import create_client, Client

# 기본 Supabase 연결 정보 (두호/국제 프로젝트)
SUPABASE_URL = "https://jqzxvdjmcfspskqvvkbk.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impxenh2ZGptY2ZzcHNrcXZ2a2JrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkzOTAzMDgsImV4cCI6MjA3NDk2NjMwOH0.NWrbS2d64sbx5q1ZEBsrg5d052hsD89_MHZ0iGd7mnE"

# Aegis-Demo 프로젝트용 별도 Supabase 연결 정보
# TODO: Aegis-Demo Supabase 프로젝트의 URL과 키로 업데이트 필요
SUPABASE_DEMO_URL = os.getenv("SUPABASE_DEMO_URL", None)
SUPABASE_DEMO_KEY = os.getenv("SUPABASE_DEMO_KEY", None)

# DB 모드 선택
USE_SUPABASE = True  # True: Supabase 사용, False: SQLite 사용 (롤백용)

# 연결 타임아웃 설정
SUPABASE_TIMEOUT = 10  # 10초 타임아웃

# SQLite 백업 경로 (만약을 대비)
SQLITE_DB_PATH = "../database/wip_database.db"
SQLITE_BACKUP_PATH = "../database/wip_database_backup.db"

# 공정 단계 정의
PROCESS_STAGES = {
    'CUT': '절단/절곡',
    'LASER_PIPE': 'P레이저(파이프)',
    'LASER_SHEET': '레이저(판재)',
    'BAND': '벤딩',
    'PAINT': '페인트',
    'STICKER': '스티커',
    'RECEIVING': '입고'
}

# Supabase 클라이언트 캐시
@st.cache_resource(show_spinner=False)
def get_supabase_client(url: str = None, key: str = None) -> Client:
    """
    Supabase 클라이언트를 반환합니다.

    Args:
        url: Supabase URL (None이면 기본값 사용)
        key: Supabase API Key (None이면 기본값 사용)

    Returns:
        Supabase Client 인스턴스
    """
    _url = url or SUPABASE_URL
    _key = key or SUPABASE_KEY

    if not _url or not _key:
        raise RuntimeError("Supabase 접속정보가 없습니다. SUPABASE_URL / SUPABASE_KEY 설정 확인")

    return create_client(_url, _key)


# AuthManager 인스턴스를 생성하는 함수 추가
def get_auth_manager():
    """AuthManager 인스턴스를 반환합니다."""
    from auth.auth_manager import AuthManager
    return AuthManager(SUPABASE_URL, SUPABASE_KEY)
