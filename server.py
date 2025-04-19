from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# السماح لكل origins بالوصول
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يمكنك تخصيصها إذا كنت تريد السماح لمصادر معينة
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/check-ngrok")
async def check_ngrok(url: str = None):
    if not url:
        raise HTTPException(status_code=400, detail="يرجى تمرير رابط ngrok في البراميتر ?url=")

    try:
        response = requests.get(url, timeout=5)
        html_content = response.text

        return JSONResponse(content={
            "success": True,
            "content": html_content
        })

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

# لتشغيل التطبيق
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
