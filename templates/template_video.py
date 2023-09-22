<!-- templates/video_list.html -->
{% for video in videos %}
  <h2>{{ video.title }}</h2>
  <p>{{ video.description }}</p>
  <a href="{% url 'video_detail' video.id %}">Watch video</a>
{% endfor %}
 
<!-- templates/video_detail.html -->
<h2>{{ video.title }}</h2>
<p>{{ video.description }}</p>
<video controls>
  <source src="{{ video.video.url }}" type="{{ video.video.mimetype }}">
