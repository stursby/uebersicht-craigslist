url = 'http://minneapolis.craigslist.org/search/sss?query=bmw+m3&sort=date'

command: "python ./craigslist/craigslist.widget/app.py #{url}"
# OR uncomment this one if you only have the "craigslist.widget" folder
# command: "python ./craigslist.widget/app.py #{url}"

refreshFrequency: 600000 # ms (10 minutes)

render: -> """
  <link href='http://fonts.googleapis.com/css?family=Roboto+Condensed:400,700' rel='stylesheet' type='text/css'>
  <ul class="posts cf">
  </ul>
  """

update: (output, domEl) ->
  posts = JSON.parse(output)
  ul = $(domEl).find('ul')

  ul.html ''

  renderPost = (post) ->
    """
    <li class="post">
      <a href="#{ post.link }">
      <div class="left">
        <div class="image" style="background-image: url(#{ post.image });"></div>
      </div>
      <div class="right">
        <div class="title">#{ post.title }</div>
        <div class="date">#{ post.date }</div>
      </div>
      </a>
    </li>
    """

  for post in posts
    ul.append renderPost(post)

style: """
  width: 100%
  left: 20px
  top: 20px
  color: #000
  overflow: hidden
  max-width: 300px
  background: rgba(255, 255, 255, 0.2)
  border-radius: 5px
  color: white
  font-family: 'Roboto Condensed', sans-serif
  -webkit-font-smoothing: antialiased

  a 
    color: inherit

  *
    box-sizing: border-box;
    margin: 0
    padding: 0

  .post
    list-style: none
    float: left
    width: 100%
    height: auto
    display: inline-block
    padding: 10px
    border-bottom: 1px solid rgba(255, 255, 255, 0.3)

  .post:last-child
    border-bottom: none

  .left, .right
    float: left
    height: 50px

  .left
    width: 20%

  .right
    width: 80%
    padding-top: 7px
    line-height: 1.2
    text-indent: 3px

  .cf:before,
  .cf:after
    content: " "; /* 1 */
    display: table; /* 2 */

  .cf:after
    clear: both

  .image
    width: 50px;
    height: 50px
    border-radius: 50%
    background-size: cover

  .date
    font-weight: 800
    font-size: 14px
    opacity: 0.8

  .title
    white-space: nowrap
    text-overflow: ellipsis
    overflow: hidden

"""