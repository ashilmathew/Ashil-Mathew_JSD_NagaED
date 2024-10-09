from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn


app = FastAPI()


class Course(BaseModel):
    id: int
    title: str
    description: str
    duration: str  # Example: "4 weeks"


courses_db: List[Course] = []


@app.post("/courses/", response_model=Course)
def create_course(course: Course):
    for existing_course in courses_db:
        if existing_course.id == course.id:
            raise HTTPException(status_code=400, detail="Course ID already exists")
    courses_db.append(course)
    return course


@app.get("/courses/", response_model=List[Course])
def get_all_courses():
    return courses_db


@app.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int):
    for course in courses_db:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")


@app.put("/courses/{course_id}", response_model=Course)
def update_course(course_id: int, updated_course: Course):
    for index, course in enumerate(courses_db):
        if course.id == course_id:
            courses_db[index] = updated_course
            return updated_course
    raise HTTPException(status_code=404, detail="Course not found")


@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    for index, course in enumerate(courses_db):
        if course.id == course_id:
            del courses_db[index]
            return {"message": "Course deleted successfully"}
    raise HTTPException(status_code=404, detail="Course not found")



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
