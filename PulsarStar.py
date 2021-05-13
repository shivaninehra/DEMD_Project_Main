from pydantic import BaseModel

class PulsarStars(BaseModel):
    meanintprofile : float
    stdintprofile : float
    skewintprofile : float
    meandmsnr : float
    exckurtdmsnr : float
