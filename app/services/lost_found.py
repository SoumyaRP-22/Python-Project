from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.db import get_db
from app.models import LostFoundItem, User
from app.schema import LostFoundCreate, LostFoundOut
from app.core.security import get_current_user, require_admin

router= APIRouter()

# ----------------------------
# POST /lost-found       
# ----------------------------
@router.post("/lost_found" , response_model=LostFoundOut)
def create_item(payload: LostFoundCreate, db: Session=Depends(get_db)):
    new_item=LostFoundItem(
        title=payload.title,
        description=payload.description,
        is_found=payload.is_found
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item



# ----------------------
# GET /lost-found        
# ----------------------
@router.get("/lost-found",response_model=List[LostFoundOut])
def list_lost_found_items(db:Session=Depends(get_db)):
    items=db.query(LostFoundItem).order_by(LostFoundItem.created_at.desc()).all()
    return items



# -----------------------------
# GET /lost-found/{id}       
# -----------------------------
@router.get("/lost-found/{id}",response_model=LostFoundOut)
def get_lost_found_item(id:int,db:Session=Depends(get_db)):
    item=db.query(LostFoundItem).filter(LostFoundItem.id==id).first()
    if not item:
        raise HTTPException(status_code=404,detail="Item not found")
    return item



# ----------------------------------------
# GET /admin/lost-found/{id}/delete       
# ----------------------------------------
@router.delete("/admin/lost_found/{id}/delete")
def delete_item(
    id: int,
    db: Session=Depends(get_db),
    _: User=Depends(require_admin)
):
    item = db.query(LostFoundItem).filter(LostFoundItem.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return{"message": "Item deleted successfully"}
