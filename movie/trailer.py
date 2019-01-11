import mediafile
import fresh_tomatoes
bahubali2=mediafile.movies("bahubali the conclusion","revenge drama","http://www.cinemagala.com/gallery/events/prabhas-anushka-3-arrow-photos-bahubali2/Babubali%20prabhas%20arrow%20posters.jpg","https://youtu.be/cW5iMY2Zgbs")
bahubali1=mediafile.movies("bahubali the beggining","revenge drama","https://www.filmibeat.com/img/2015/07/10-1436528680-reasonstowatchbaahubalitamil.jpg","https://youtu.be/QSVE6YWSGlw")
rhymes=mediafile.movies("children rhymes","rhymes","https://i.ytimg.com/vi/-IPKPz1pujM/hqdefault.jpg","https://youtu.be/-IPKPz1pujM")
robo=mediafile.movies("robo","scientific movie","http://www.cinejosh.com/gallereys/movies/normal/robo_movie_latest_gallery/robo_movie_latest_gallery_008.jpg","https://youtu.be/PoPv-Ss6YbI")
kick=mediafile.movies("kick","entertainment movie","https://i.pinimg.com/originals/e6/57/ab/e657abf8621930f57fee3cbbf8a90c0f.jpg","https://youtu.be/CgqFtkID7fk")
srimanthudu=mediafile.movies("srimanthudu","family entertainment","https://wallpaper-house.com/data/out/7/wallpaper2you_196979.jpg","https://youtu.be/6_pvmYhWWHc")
movies=[bahubali2,bahubali1,rhymes,robo,kick,srimanthudu]
fresh_tomatoes.open_movies_page(movies)
