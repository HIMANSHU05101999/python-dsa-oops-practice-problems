# OOP Revision Exercise 18
#
# Movie Collection
#
# Difficulty: ★★★☆☆
#
# Movie
#
# Stores:
# - title
# - rating (1-10)
# - duration
#
#
# MovieCollection
#
# Dictionary:
#
# movie_title -> Movie object
#
#
# add_movie(movie)
#
# If the movie already exists,
# keep whichever object has the HIGHER rating.
#
#
# statistics()
#
# Print:
#
# total movies
# average rating
# highest rated movie
#
#
# Also print rating distribution:
#
# 10:
# 9:
# 8:
# ...
# 1:
#
# using x characters.

class Movie:
    def __init__(self, title: str, rate: int, duration: int):
        self.__title=title
        self.__rate=rate
        self.__duration=duration

    @property
    def title(self):
        return self.__title

    @property
    def rate(self):
        return self.__rate

    @property
    def duration(self):
        return self.__duration

    @rate.setter
    def rate(self,val):
        self.__rate=val

    def __str__(self):
        return f"title: {self.__title} rate: {self.__rate} duration: {self.__duration}"
    
class MovieCollection:
    def __init__(self):
        self.__movie_collection={}

    def add_movie(self):
        title=input("Enter Title: ")
        rate=int(input("Enter rating: "))
        duration=int(input("Enter duration: "))
        movie_obj=Movie(title,rate,duration)

        if title in self.__movie_collection:
            if rate>self.__movie_collection[title].rate:
                self.__movie_collection[title].rate=movie_obj.rate
        else:
            self.__movie_collection[title]=movie_obj

    def view(self):
        for movie in self.__movie_collection:
            print(self.__movie_collection[movie])


    def stats(self):
        if not self.__movie_collection:
            return
        
        total_movie=len(self.__movie_collection)
        total_rate=0
        highest_rate=0

        stat={0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:""}

        for _,obj in self.__movie_collection.items():
            total_rate+=obj.rate
            if highest_rate<obj.rate:
                highest_rate=obj.rate
            if obj.rate in stat:
                stat[obj.rate]+="x"
        average_rating=total_rate/total_movie
        print()
        print(f"Total Movies: {total_movie}")
        print(f"Average Rating: {average_rating}")
        print(f"Highest Rating: {highest_rate}")
        print()
        print("Statistics: ")
        print()
        for rate,val in stat.items():
            print(f"{rate}: {val}")


    def interface(self):
        print("1 add movie")
        print("2 stats")
        print("3 view")
        while True:
            pick=input("Pick:")
            if pick=="1":
                self.add_movie()
            if pick=="2":
                self.stats()
            if pick=="3":
                self.view()
            if pick=="0":
                return
    

run=MovieCollection()
run.interface()
              
# total movies
# average rating
# highest rated movie


    
        