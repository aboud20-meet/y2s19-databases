from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "article"
	link = Column(String, primary_key= True)
	name = Column(String)
	topic = Column(String)
	rating = Column(Integer)

	def __repr__(self):
		return("Article Name: {}\n"
				"Artcile Topic: {}\n"
				"Article Link: {}\n"
				"Article Rating:{}\n").format(self.name, self.topic, self.link, self.rating)

	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the arknowledge


a = Knowledge(name = "15 Best Restraunts in Ohio", link = "https://www.thrillist.com/eat/cleveland/the-15-best-restaurants-in-ohio",topic = "Dining", rating = 7)
b = Knowledge(name = "5 Best things to do in Fayettville, WV", link = "https://www.tripadvisor.com/Attractions-g59058-Activities-Fayetteville_West_Virginia.html", topic = "Travel", rating = 4)
c = Knowledge(name = "Timeline of James Charles and Tati's Drama Explained", link = "https://www.elle.com/beauty/makeup-skin-care/a27453234/james-charles-tati-westbrook-youtube-drama-timeline", topic = "Drama", rating = 1)

print(repr(Knowledge.__tablename__))
print(a)

