import os
import time


class FileHelper:
    @staticmethod
    def wait_for_download(file_path, timeout=30) -> bool:
        """Ожидает, пока файл полностью появится на диске (без расширения .crdownload)"""
        end_time = time.time() + timeout
        while time.time() < end_time:
            if os.path.exists(file_path) and not file_path.endswith('.crdownload'):
                if os.path.getsize(file_path) > 0:
                    return True
            time.sleep(1)
        return False

    @staticmethod
    def get_file_size_mb(file_path) -> float:
        """Вычисляет размер файла в МБ"""
        size_bytes = os.path.getsize(file_path)
        return round(size_bytes / (1024 * 1024), 2)

    @staticmethod
    def delete_if_exists(file_path) -> None:
        """Удаляет файл"""
        if os.path.exists(file_path):
            os.remove(file_path)
