from datetime import datetime


class HealthService:

    @staticmethod
    def get_health_status():
        return {
            "status": "ok",
            "timestamp": datetime.utcnow().isoformat(),
            "service": "backend",
        }