import sqltap
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class SqlTapMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        """
        has issues
        - None object at sqltap/templates/html.mako:204
        - bytes not string at sqltap/sqltap.py:399
        """
        profiler = sqltap.start()
        response = await call_next(request)
        statistics = profiler.collect()
        sqltap.report(statistics, 'report.html', report_format='html')
        return response
