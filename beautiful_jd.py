# -*- coding: utf-8 -*-
import json
import re

import requests
from bs4 import BeautifulSoup

# page = 1
# # res = requests.get('https://movie.douban.com/subject/25790761/comments?status=P')
# res = requests.get('https://sclub.jd.com/comment/productPageComments.action?productId=5089239&score=0&sortType=5&page='+page+'&pageSize=10&isShadowSku=0&rid=0&fold=1')
#
# content = res.text
# print content
# x = '''<!DOCTYPE html>
# <html lang="zh-cmn-Hans" class="">
# <head>
#     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
#     <meta name="renderer" content="webkit">
#     <meta name="referrer" content="always">
#     <title>东方快车谋杀案 短评</title>
#
#     <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
#     <meta http-equiv="Pragma" content="no-cache">
#     <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
#
#     <meta name="keywords" content="东方快车谋杀案,Murder on the Orient Express,影讯,排片,放映时间,电影票价,在线购票"/>
#     <meta name="description" content="东方快车谋杀案短评" />
#     <meta name="mobile-agent" content="format=html5; url=http://m.douban.com/movie/subject/25790761/comments"/>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
#
#     <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
#     <link href="https://img3.doubanio.com/f/shire/94213e812acbb00123f685909b4768bb304d16f3/css/douban.css" rel="stylesheet" type="text/css">
#     <link href="https://img3.doubanio.com/f/shire/ae3f5a3e3085968370b1fc63afcecb22d3284848/css/separation/_all.css" rel="stylesheet" type="text/css">
#     <link href="https://img3.doubanio.com/f/movie/8864d3756094f5272d3c93e30ee2e324665855b0/css/movie/base/init.css" rel="stylesheet">
#     <script type="text/javascript">var _head_start = new Date();</script>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/1efae2c2d48b407a9bed76b9dd5dd8de37a8dbe1/js/douban.js"></script>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js"></script>
#
#     <style type="text/css"></style>
#     <style type="text/css">img { max-width: 100%; }</style>
#     <script type="text/javascript"></script>
#     <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/13a836970108bf09.css">
#
#     <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
# </head>
#
# <body>
#
#     <script type="text/javascript">var _body_start = new Date();</script>
#
#
#
#
#
#
#     <link href="//img3.doubanio.com/dae/accounts/resources/321e246/shire/bundle.css" rel="stylesheet" type="text/css">
#
#
#
# <div id="db-global-nav" class="global-nav">
#   <div class="bd">
#
# <div class="top-nav-info">
#   <a href="https://www.douban.com/accounts/login?source=movie" class="nav-login" rel="nofollow">登录</a>
#   <a href="https://www.douban.com/accounts/register?source=movie" class="nav-register" rel="nofollow">注册</a>
# </div>
#
#
#
# <div class="top-nav-doubanapp">
#   <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
#   <div id="top-nav-appintro" class="more-items">
#     <p class="appintro-title">豆瓣</p>
#     <p class="slogan">我们的精神角落</p>
#     <p class="qrcode">扫码直接下载</p>
#     <div class="download">
#       <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
#       <span>·</span>
#       <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
#     </div>
#     <div id="doubanapp-tip">
#       <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 5.0 全新发布</a>
#       <a href="javascript: void 0;" class="tip-close">×</a>
#     </div>
#   </div>
# </div>
#
#
#
#
# <div class="global-nav-items">
#   <ul>
#     <li class="">
#       <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
#     </li>
#     <li class="">
#       <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
#     </li>
#     <li class="on">
#       <a href="https://movie.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
#     </li>
#     <li class="">
#       <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
#     </li>
#     <li class="">
#       <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
#     </li>
#     <li class="">
#       <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
#     </li>
#     <li class="">
#       <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
#     </li>
#     <li class="">
#       <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
#     </li>
#     <li class="">
#       <a href="https://www.douban.com/time&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
#     </li>
#     <li class="">
#       <a href="https://dongxi.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-commodity&quot;,&quot;uid&quot;:&quot;0&quot;}">东西</a>
#     </li>
#     <li class="">
#       <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">市集</a>
#     </li>
#     <li>
#       <a href="#more" class="bn-more"><span>更多</span></a>
#       <div class="more-items">
#         <table cellpadding="0" cellspacing="0">
#           <tbody>
#             <tr>
#               <td>
#                 <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣摄影</a>
#               </td>
#             </tr>
#           </tbody>
#         </table>
#       </div>
#     </li>
#   </ul>
# </div>
#
#   </div>
# </div>
# <script>
#   ;window._GLOBAL_NAV = {
#     DOUBAN_URL: "https://www.douban.com",
#     N_NEW_NOTIS: 0,
#     N_NEW_DOUMAIL: 0
#   };
# </script>
#
#
#
#     <script src="//img3.doubanio.com/dae/accounts/resources/321e246/shire/bundle.js" defer="defer"></script>
#
#
#
#
#
#
#
#
#     <link href="//img3.doubanio.com/dae/accounts/resources/321e246/movie/bundle.css" rel="stylesheet" type="text/css">
#
#
#
#
# <div id="db-nav-movie" class="nav">
#   <div class="nav-wrap">
#   <div class="nav-primary">
#     <div class="nav-logo">
#       <a href="https:&#47;&#47;movie.douban.com">豆瓣电影</a>
#     </div>
#     <div class="nav-search">
#       <form action="https:&#47;&#47;movie.douban.com/subject_search" method="get">
#         <fieldset>
#           <legend>搜索：</legend>
#           <label for="inp-query">
#           </label>
#           <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="电影、影人、影院、电视剧" value=""></div>
#           <div class="inp-btn"><input type="submit" value="搜索"></div>
#           <input type="hidden" name="cat" value="1002" />
#         </fieldset>
#       </form>
#     </div>
#   </div>
#   </div>
#   <div class="nav-secondary">
#
#
# <div class="nav-items">
#   <ul>
#     <li    ><a href="https://movie.douban.com/cinema/nowplaying/"
#      >影讯&购票</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/explore"
#      >选电影</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/tv/"
#      >电视剧</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/chart"
#      >排行榜</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/tag/"
#      >分类</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/review/best/"
#      >影评</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/annual2016/?source=navigation"
#      >2016年度榜单</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/standbyme/2016?source=navigation"
#      >2016观影报告</a>
#     </li>
#   </ul>
# </div>
#
#   </div>
# </div>
#
# <script id="suggResult" type="text/x-jquery-tmpl">
#   <li data-link="{{= url}}">
#             <a href="{{= url}}" onclick="moreurl(this, {from:'movie_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
#             <img src="{{= img}}" width="40" />
#             <p>
#                 <em>{{= title}}</em>
#                 {{if year}}
#                     <span>{{= year}}</span>
#                 {{/if}}
#                 {{if sub_title}}
#                     <br /><span>{{= sub_title}}</span>
#                 {{/if}}
#                 {{if address}}
#                     <br /><span>{{= address}}</span>
#                 {{/if}}
#                 {{if episode}}
#                     {{if episode=="unknow"}}
#                         <br /><span>集数未知</span>
#                     {{else}}
#                         <br /><span>共{{= episode}}集</span>
#                     {{/if}}
#                 {{/if}}
#             </p>
#         </a>
#         </li>
#   </script>
#
#
#
#
#     <script src="//img3.doubanio.com/dae/accounts/resources/321e246/movie/bundle.js" defer="defer"></script>
#
#
#
#
#
#
#     <div id="wrapper">
#
#
#
#     <div id="content">
#
#     <h1>东方快车谋杀案 短评</h1>
#
#         <div class="grid-16-8 clearfix">
#
#
#             <div class="article">
#
#
#
#
#
# <div class="clearfix Comments-hd">
#     <ul class="fleft CommentTabs">
#             <li class="is-active">
#                 <span>看过(770)</span>
#             </li>
#
#             <li>
#                 <a href="?status=F">想看(1412)</a>
#             </li>
#     </ul>
#     <div class="fright">
#         <a href="javascript:;" class="comment_btn j a_show_login" name="cbtn-25790761">我来写短评</a>
#     </div>
# </div>
#
#
#     <div class="title_line clearfix color_gray">
#         <div class="fleft Comments-sortby">
#                 <span>热门</span>
#                 <a href="?sort=time&status=P">最新</a>
#                 <a href="follows_comments?status=P" class="j a_show_login"> 好友</a>
#         </div>
#     </div>
#
#     <div class="comment-filter">
#         <label>
#             <input type="radio" name="sort" value=""  checked="checked"><span class="filter-name">全部</span><span class="comment-percent"></span>
#         </label>
#         <label>
#             <input type="radio" name="sort" value="h" ><span class="filter-name">好评</span><span class="comment-percent">53%</span>
#         </label>
#         <label>
#             <input type="radio" name="sort" value="m" ><span class="filter-name">一般</span><span class="comment-percent">37%</span>
#         </label>
#         <label>
#             <input type="radio" name="sort" value="l" ><span class="filter-name">差评</span><span class="comment-percent">10%</span>
#         </label>
#     </div>
#
#     <div class="mod-bd" id="comments">
#
#
#         <div class="comment-item" data-cid="1268214179">
#
#
#         <div class="avatar">
#             <a title="汤川影业" href="https://www.douban.com/people/55505390/">
#                 <img src="https://img3.doubanio.com/icon/u55505390-23.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">297</span>
#                 <input value="1268214179" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/55505390/" class="">汤川影业</a>
#                     <span>看过</span>
#                     <span class="allstar40 rating" title="推荐"></span>
#                 <span class="comment-time " title="2017-11-08 09:44:36">
#                     2017-11-08
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 中国所有的悬疑电影都应该效仿东方列车的拍摄手法，拍摄出的是一种想让人探求真相的神秘感，而不是惊吓感，这一点目前只有烈日灼心做到了
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1268708875">
#
#
#         <div class="avatar">
#             <a title="康报虹" href="https://www.douban.com/people/89528523/">
#                 <img src="https://img3.doubanio.com/icon/u89528523-10.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">114</span>
#                 <input value="1268708875" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/89528523/" class="">康报虹</a>
#                     <span>看过</span>
#                     <span class="allstar30 rating" title="还行"></span>
#                 <span class="comment-time " title="2017-11-09 12:16:50">
#                     2017-11-09
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 一定要问三遍的是：
# 为什么不让Depp演Poirot！
# 为什么不让Depp演Poirot！
# 为什么不让Depp演Poirot！
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1267723624">
#
#
#         <div class="avatar">
#             <a title="光头" href="https://www.douban.com/people/63870964/">
#                 <img src="https://img1.doubanio.com/icon/u63870964-9.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">46</span>
#                 <input value="1267723624" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/63870964/" class="">光头</a>
#                     <span>看过</span>
#                     <span class="allstar20 rating" title="较差"></span>
#                 <span class="comment-time " title="2017-11-07 04:32:45">
#                     2017-11-07
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 第一次看70mm放映，可惜演员之间没啥化学反应，表演都压着，为低调奢华而减小表演尺度，实际上并不细腻反而大家自己都摸不着头脑，几段有爆点的也都压在了导演饰演的男主角身上，然而此君一咆哮就穿越到了莎士比亚剧场……
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1187866649">
#
#
#         <div class="avatar">
#             <a title="\t^h/" href="https://www.douban.com/people/terry_f/">
#                 <img src="https://img1.doubanio.com/icon/u2520407-279.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">25</span>
#                 <input value="1187866649" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/terry_f/" class="">\t^h/</a>
#                     <span>看过</span>
#                     <span class="allstar20 rating" title="较差"></span>
#                 <span class="comment-time " title="2017-11-09 15:50:53">
#                     2017-11-09
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 事实证明，演技好也拯救不了自恋型自导自演各种加戏。风光浓浓的CGI痕迹，反倒让整体非常廉价。至于那个被各种吹的最后的晚餐的构图，只想说当年的条件Lumet都敢挑战局促空间里的群戏，这部电影的最大意义就是让人看到Lumet多牛吧
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1267576926">
#
#
#         <div class="avatar">
#             <a title="喵尔摩丝" href="https://www.douban.com/people/dorothy_cullen/">
#                 <img src="https://img3.doubanio.com/icon/u44370220-13.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">74</span>
#                 <input value="1267576926" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/dorothy_cullen/" class="">喵尔摩丝</a>
#                     <span>看过</span>
#                     <span class="allstar40 rating" title="推荐"></span>
#                 <span class="comment-time " title="2017-11-06 21:07:00">
#                     2017-11-06
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 非常典型的KBTC风格，几幕黑白镜头很有罗密欧与茱丽叶的调调，所以其实并不算原汁原味的改编，说是“作者电影”更恰如其分。审讯戏的平行剪辑太出彩，高潮段落酷似《最后的晚餐》的构图一出，惊起我一身鸡皮疙瘩。肯爷或许不是最好的storyteller，但不可否认他是极具创造力的艺术家。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1266686669">
#
#
#         <div class="avatar">
#             <a title="Lyu WEN" href="https://www.douban.com/people/52447788/">
#                 <img src="https://img3.doubanio.com/icon/u52447788-15.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">51</span>
#                 <input value="1266686669" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/52447788/" class="">Lyu WEN</a>
#                     <span>看过</span>
#                     <span class="allstar30 rating" title="还行"></span>
#                 <span class="comment-time " title="2017-11-05 00:45:22">
#                     2017-11-05
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 强尼戴普死了以后我就睡着了
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1267697839">
#
#
#         <div class="avatar">
#             <a title="几根佩毛" href="https://www.douban.com/people/peitingli/">
#                 <img src="https://img3.doubanio.com/icon/u120395031-20.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">45</span>
#                 <input value="1267697839" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/peitingli/" class="">几根佩毛</a>
#                     <span>看过</span>
#                     <span class="allstar30 rating" title="还行"></span>
#                 <span class="comment-time " title="2017-11-07 01:04:10">
#                     2017-11-07
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 看得昏昏欲睡，没有想得那么好。然后下一部尼罗河惨案🌚
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1265068906">
#
#
#         <div class="avatar">
#             <a title="突然粉碎" href="https://www.douban.com/people/4051316/">
#                 <img src="https://img1.doubanio.com/icon/u4051316-9.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">46</span>
#                 <input value="1265068906" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/4051316/" class="">突然粉碎</a>
#                     <span>看过</span>
#                     <span class="allstar40 rating" title="推荐"></span>
#                 <span class="comment-time " title="2017-11-06 21:50:45">
#                     2017-11-06
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 《尼罗河上的惨案》超长预告片，一次中庸却有趣的改编，结局毫不意外泪点还是被击中，用自己的方式找回正义时的大快人心，真凶揭晓时的怅然若失，连同摄影配乐都值得玩味，肯爵舞台剧功底尽显，大侦探波洛是最可爱的强迫症，比利时口音很喜感，群戏不及老版，感叹Michelle Pfeiffer美人依旧爆发力惊人
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1267604982">
#
#
#         <div class="avatar">
#             <a title="Ron Chan" href="https://www.douban.com/people/RonChan/">
#                 <img src="https://img1.doubanio.com/icon/u42050757-59.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">19</span>
#                 <input value="1267604982" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/RonChan/" class="">Ron Chan</a>
#                     <span>看过</span>
#                     <span class="allstar30 rating" title="还行"></span>
#                 <span class="comment-time " title="2017-11-06 22:01:20">
#                     2017-11-06
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 吕美特的版本更加的踏实牢靠，且曲折，这一版相对要华丽很多，且在一些细节上加入了一些容易被现代人所接受的小幽默，完成度还算不错，但也难有突破，且对人物的刻画不及老版深入。最后一场戏，米歇尔·菲弗的表演大赞，之前英格丽·褒曼的那个角色这次在佩内洛普·克鲁兹的表演下变得有点可有可无了。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1268106392">
#
#
#         <div class="avatar">
#             <a title="羚羊的灵魂" href="https://www.douban.com/people/clzleo/">
#                 <img src="https://img1.doubanio.com/icon/u59237362-8.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">21</span>
#                 <input value="1268106392" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/clzleo/" class="">羚羊的灵魂</a>
#                     <span>看过</span>
#                     <span class="allstar30 rating" title="还行"></span>
#                 <span class="comment-time " title="2017-11-07 23:44:42">
#                     2017-11-07
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 太平庸了 德普在海报最大纯属骗钱
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1255476960">
#
#
#         <div class="avatar">
#             <a title="锐利修蕊" href="https://www.douban.com/people/ruilixiurui/">
#                 <img src="https://img3.doubanio.com/icon/u12544519-52.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">25</span>
#                 <input value="1255476960" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/ruilixiurui/" class="">锐利修蕊</a>
#                     <span>看过</span>
#                     <span class="allstar30 rating" title="还行"></span>
#                 <span class="comment-time " title="2017-11-06 21:09:00">
#                     2017-11-06
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 三星半吧，可能冬天了，最近看电影很煽情的段落都有点控制不住开始啜泣。肯尼斯布拉纳的后现代新古典主义改编，最终的结局处理，以「最后的晚餐」进行推理对峙的审判，可结果竟然是面相自己。用一个众所周知的名著，正义对法律虚构，直指悲壮的现实呈现。愿每个人都能够以不同方式维护自己内心的安宁。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1267604275">
#
#
#         <div class="avatar">
#             <a title="一口吃掉小蛋糕" href="https://www.douban.com/people/cheesecakehouse/">
#                 <img src="https://img3.doubanio.com/icon/u2456828-173.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">47</span>
#                 <input value="1267604275" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/cheesecakehouse/" class="">一口吃掉小蛋糕</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2017-11-06 21:59:59">
#                     2017-11-06
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 一个有新意的老故事。有多爱，就有多恨，仇恨会将人击得粉碎，只有心存善念，灵魂才得以拯救。德普彻底走出船长的影子，最美猫女风韵犹存。剧情没有特别多的改动，拍摄手法很“波洛”，宛如强迫症一般的规整。配乐非常精彩，大提琴一起，仇恨烟消云。有中文译制版，值得二刷。期待尼罗河上的惨案。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1267243329">
#
#
#         <div class="avatar">
#             <a title="Lunansane" href="https://www.douban.com/people/lunamu/">
#                 <img src="https://img3.doubanio.com/icon/u3315460-26.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">10</span>
#                 <input value="1267243329" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/lunamu/" class="">Lunansane</a>
#                     <span>看过</span>
#                     <span class="allstar20 rating" title="较差"></span>
#                 <span class="comment-time " title="2017-11-06 03:19:46">
#                     2017-11-06
#                 </span>
#             </span>
#         </h3>
#         <p class=""> ...... 太一言难尽了 完全没有悬疑感 被肯爵爷拍的如同人性大讲堂 还有波罗的超英秀 难道是爷爷嫌自己早生了三十年没有赶上现在的风潮？ 那请不要浪费我阿的本子嘛。。。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1268763468">
#
#
#         <div class="avatar">
#             <a title="荔枝超人" href="https://www.douban.com/people/richer725/">
#                 <img src="https://img3.doubanio.com/icon/u1114759-42.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">6</span>
#                 <input value="1268763468" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/richer725/" class="">荔枝超人</a>
#                     <span>看过</span>
#                     <span class="allstar30 rating" title="还行"></span>
#                 <span class="comment-time " title="2017-11-09 14:41:25">
#                     2017-11-09
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 看得出一些别出心裁的运镜和精心的编排，不过整体感觉还是导演+男一用来自恋的。熟练明星不少，不过都比不上你们的德普又一次金酸梅级别的演出亮眼。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1268758078">
#
#
#         <div class="avatar">
#             <a title="喵驼酱°" href="https://www.douban.com/people/49349129/">
#                 <img src="https://img3.doubanio.com/icon/u49349129-22.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">4</span>
#                 <input value="1268758078" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/49349129/" class="">喵驼酱°</a>
#                     <span>看过</span>
#                     <span class="allstar40 rating" title="推荐"></span>
#                 <span class="comment-time " title="2017-11-09 14:28:06">
#                     2017-11-09
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 想知道脸盲营销号写这部电影里有凯拉奈特利的时候到底是把佩内洛普克鲁兹还是黛西雷德利认成了她，观影过程中还有人大声猜凶手也是搞笑。看过大部分演员演的莎剧所以可以欣然接受并享受所谓的drama感，最后的晚餐的构图也契合了这种感觉。话说怎么还没有高订找导演拍广告啊！！
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1268813448">
#
#
#         <div class="avatar">
#             <a title="文白" href="https://www.douban.com/people/46815070/">
#                 <img src="https://img3.doubanio.com/icon/u46815070-3.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">6</span>
#                 <input value="1268813448" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/46815070/" class="">文白</a>
#                     <span>看过</span>
#                     <span class="allstar30 rating" title="还行"></span>
#                 <span class="comment-time " title="2017-11-09 16:47:37">
#                     2017-11-09
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 画面很漂亮。其实推理，尤其是耳熟能详的推理，翻拍起来有着天然的劣势。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1267681544">
#
#
#         <div class="avatar">
#             <a title="杀手里昂Leon" href="https://www.douban.com/people/4026585/">
#                 <img src="https://img3.doubanio.com/icon/u4026585-2.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">21</span>
#                 <input value="1267681544" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/4026585/" class="">杀手里昂Leon</a>
#                     <span>看过</span>
#                     <span class="allstar40 rating" title="推荐"></span>
#                 <span class="comment-time " title="2017-11-07 00:21:11">
#                     2017-11-07
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 电影感很强，用长镜头带出众生相，用上帝视角的俯拍呈现谋杀案，用镜子叠影展现每个人物内心的隐秘。结尾“最后的晚餐”式构图，将12个人正义的复仇推向极致，也让波洛遭遇情与法的道德困境。这也是这次改编最为迷人之处，波洛一开始认为凡事只有对错，没有灰色地带，最后却将天平砝码放在道德情理一边
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1266748436">
#
#
#         <div class="avatar">
#             <a title="木上立" href="https://www.douban.com/people/ewan7/">
#                 <img src="https://img3.doubanio.com/icon/u37234365-90.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">12</span>
#                 <input value="1266748436" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/ewan7/" class="">木上立</a>
#                     <span>看过</span>
#                     <span class="allstar20 rating" title="较差"></span>
#                 <span class="comment-time " title="2017-11-05 07:33:27">
#                     2017-11-05
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 卡司和观众一起走神，CG场景的过度使用，使片子‘电影感’尽失，唯一精彩的部分也并不属于影片的制作，而是阿加莎的故事。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1269068276">
#
#
#         <div class="avatar">
#             <a title="结冰" href="https://www.douban.com/people/caiyanbin/">
#                 <img src="https://img3.doubanio.com/icon/u44203357-95.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">4</span>
#                 <input value="1269068276" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/caiyanbin/" class="">结冰</a>
#                     <span>看过</span>
#                     <span class="allstar30 rating" title="还行"></span>
#                 <span class="comment-time " title="2017-11-10 08:07:34">
#                     2017-11-10
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 布拉纳可能忘了，这是一个13人的群戏，死命给自己加戏，完成了一场个人秀。别再拍了，谢谢你。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1268869511">
#
#
#         <div class="avatar">
#             <a title="光头" href="https://www.douban.com/people/donotgo/">
#                 <img src="https://img3.doubanio.com/icon/u2524939-10.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">5</span>
#                 <input value="1268869511" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/donotgo/" class="">光头</a>
#                     <span>看过</span>
#                     <span class="allstar10 rating" title="很差"></span>
#                 <span class="comment-time " title="2017-11-09 19:27:09">
#                     2017-11-09
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 反胃。能不能别再侮辱阿婆的小说了？另外片尾看到老雷居然是这部片的制片人之一。有没有搞错，老雷你到底哪里想不开了。
#         </p>
#     </div>
#
#         </div>
#
#
#
#             <div class="comments-footer-tips">
#                 * 影片上映之前的、与影片无关的或包含人身攻击等内容的短评都将有可能被折叠，且评分不计入豆瓣评分。<br/>
#                 * 短评的排序是将豆瓣成员的投票加权平均计算后的结果，通过算法的调校，更好地反映短评内容的价值。<br/>
#             </div>
#
#         <div id="paginator" class="center">
#                 <span class="first"><< 首页</span>
#                 <span class="prev">< 前页</span>
#                 <a href="?start=20&amp;limit=20&amp;sort=new_score&amp;status=P&amp;percent_type=" data-page="" class="next">后页 ></a>
#         </div>
#
#
#
#
#
#
#     </div>
#
#             </div>
#             <div class="aside">
#
#
#
# <p class="pl2">&gt; <a href="https://movie.douban.com/subject/25790761/">去 东方快车谋杀案 的页面</a></p>
#
#     <div class="indent">
#
#
#
#
#
#
#
#
#
#
# <div class="movie-summary">
#         <div class="movie-pic"><a  href="https://movie.douban.com/subject/25790761/" ><img alt="东方快车谋杀案 Murder on the Orient Express" title="东方快车谋杀案 Murder on the Orient Express" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2504371024.jpg" rel="v:image" width="100px"></a></div>
#     <span class="attrs">
#
#
#         <p>
#             <span class="pl">导演:</span>
#                 <a  href="https://movie.douban.com/celebrity/1036342/">肯尼思·布拉纳</a>
#         </p>
#
#
#
#         <p>
#             <span class="pl">主演:</span>
#                 <a  href="https://movie.douban.com/celebrity/1036342/">肯尼思·布拉纳</a> / <a  href="https://movie.douban.com/celebrity/1005774/">佩内洛普·克鲁兹</a> / <a  href="https://movie.douban.com/celebrity/1010539/">威廉·达福</a> / <a  href="https://movie.douban.com/celebrity/1054384/">朱迪·丹奇</a> / <a  href="https://movie.douban.com/celebrity/1054456/">约翰尼·德普</a> / <a  href="https://movie.douban.com/celebrity/1305235/">乔什·加德</a> / <a  href="https://movie.douban.com/celebrity/1027866/">德里克·雅各比</a> / <a  href="https://movie.douban.com/celebrity/1179291/">小莱斯利·奥多姆</a> / <a  href="https://movie.douban.com/celebrity/1035642/">米歇尔·菲佛</a> / <a  href="https://movie.douban.com/celebrity/1339916/">黛西·雷德利</a> / <a  href="https://movie.douban.com/celebrity/1310841/">露西·宝通</a> / <a  href="https://movie.douban.com/celebrity/1004900/">奥利维娅·科尔曼</a> / <a  href="https://movie.douban.com/celebrity/1017985/">亚当·加西亚</a> / <a  href="https://movie.douban.com/celebrity/1148600/">米兰达·莱森</a> / <a  href="https://movie.douban.com/celebrity/1249341/">曼努埃尔·加西亚-鲁尔福</a> / <a  href="https://movie.douban.com/celebrity/1328705/">汤姆·巴特曼</a> / <a  href="https://movie.douban.com/celebrity/1273062/">马尔万·肯扎里</a> / <a  href="https://movie.douban.com/celebrity/1232518/">阿拉·萨菲</a> / <a  href="https://movie.douban.com/celebrity/1347954/">瑟盖·普罗宁</a>
#         </p>
#
#
#
#         <p>
#             <span class="pl">类型:</span>
#                 剧情, 犯罪, 悬疑
#         </p>
#
#
#
#         <p>
#             <span class="pl">地区:</span>
#                 美国
#         </p>
#
#
#
#         <p>
#             <span class="pl">片长:</span>
#                 114分钟
#         </p>
#
#
#
#         <p>
#             <span class="pl">上映:</span>
#                 2017-11-03(英国), 2017-11-10(美国), 2017-11-10(中国大陆)
#         </p>
#
#         <a  class="trail_link" data-trailer-id="223165" href="https://movie.douban.com/trailer/223165/#content" >预告片</a>
#     </span>
# </div>
#
#
#
#     </div>
#     <div id="dale_movie_subject_comments_bottom_right"></div>
#
#             </div>
#             <div class="extra">
#
#             </div>
#         </div>
#     </div>
#
#
#     <div id="footer">
#             <div class="footer-extra"></div>
#
# <span id="icp" class="fleft gray-link">
#     &copy; 2005－2017 douban.com, all rights reserved 北京豆网科技有限公司
# </span>
#
# <a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>
#
# <span class="fright">
#     <a href="https://www.douban.com/about">关于豆瓣</a>
#     · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
#     · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
#     · <a href="https://www.douban.com/about?policy=disclaimer">免责声明</a>
#
#     · <a href="https://help.douban.com/?app=movie" target="_blank">帮助中心</a>
#     · <a href="https://www.douban.com/doubanapp/">移动应用</a>
#     · <a href="https://www.douban.com/partner/">豆瓣广告</a>
# </span>
#
#     </div>
#
#     </div>
#     <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/6ea26aeaf2fafd20.js"></script>
#
#
#     <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css" />
#     <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/movie/1d829b8605b9e81435b127cbf3d16563aaa51838/css/movie/mod/reg_login_pop.css" />
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/3d185ca912c999ee7f464749201139ebf8eb6972/js/ui/dialog.js"></script>
#     <script type="text/javascript">
#         var HTTPS_DB='https://www.douban.com';
# var account_pop={open:function(o,e){e?referrer="?referrer="+encodeURIComponent(e):referrer="?referrer="+window.location.href;var n="",i="",t=382;"reg"===o?(n="用户注册",i="https://accounts.douban.com/popup/login?source=movie#popup_register",t=480):"login"===o&&(n="用户登录",i="https://accounts.douban.com/popup/login?source=movie");var r=document.location.protocol+"//"+document.location.hostname,a=dui.Dialog({width:478,title:n,height:t,cls:"account_pop",isHideTitle:!0,modal:!0,content:"<iframe scrolling='no' frameborder='0' width='478' height='"+t+"' src='"+i+"' name='"+r+"'></iframe>"},!0),c=a.node;if(c.undelegate(),c.delegate(".dui-dialog-close","click",function(){var o=$("body");o.find("#login_msk").hide(),o.find(".account_pop").remove()}),$(window).width()<478){var u="";"reg"===o?u=HTTPS_DB+"/accounts/register"+referrer:"login"===o&&(u=HTTPS_DB+"/accounts/login"+referrer),window.location.href=u}else a.open();$(window).bind("message",function(o){"https://accounts.douban.com"===o.originalEvent.origin&&(c.find("iframe").css("height",o.originalEvent.data),c.height(o.originalEvent.data),a.update())})}};Douban&&Douban.init_show_login&&(Douban.init_show_login=function(o){var e=$(o);e.click(function(){var o=e.data("ref")||"";return account_pop.open("login",o),!1})}),Do(function(){$("body").delegate(".pop_register","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("reg",e),!1}),$("body").delegate(".pop_login","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("login",e),!1})});
#     </script>
#
#
#
#
#
#
#
#
# <script type="text/javascript">
#     (function (global) {
#         var newNode = global.document.createElement('script'),
#             existingNode = global.document.getElementsByTagName('script')[0],
#             adSource = '//erebor.douban.com/',
#             userId = '',
#             browserId = 'neOHiLMBtts',
#             criteria = '3:/subject/25790761/comments?status=P',
#             preview = '',
#             debug = false,
#             adSlots = ['dale_movie_subject_comments_bottom_right'];
#
#         global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
#         global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);
#
#         newNode.setAttribute('type', 'text/javascript');
#         newNode.setAttribute('src', 'https://img3.doubanio.com/f/adjs/065ebb9955a88fb066124ae427dd039162862c4f/ad.release.js');
#         newNode.setAttribute('async', true);
#         existingNode.parentNode.insertBefore(newNode, existingNode);
#     })(this);
# </script>
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# <script type="text/javascript">
# var _paq = _paq || [];
# _paq.push(['trackPageView']);
# _paq.push(['enableLinkTracking']);
# (function() {
#     var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
#     _paq.push(['setTrackerUrl', u+'piwik']);
#     _paq.push(['setSiteId', '100001']);
#     var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
#     g.type='text/javascript';
#     g.defer=true;
#     g.async=true;
#     g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
#     s.parentNode.insertBefore(g,s);
# })();
# </script>
#
# <script type="text/javascript">
# var setMethodWithNs = function(namespace) {
#   var ns = namespace ? namespace + '.' : ''
#     , fn = function(string) {
#         if(!ns) {return string}
#         return ns + string
#       }
#   return fn
# }
#
# var gaWithNamespace = function(fn, namespace) {
#   var method = setMethodWithNs(namespace)
#   fn.call(this, method)
# }
#
# var _gaq = _gaq || []
#   , accounts = [
#       { id: 'UA-7019765-1', namespace: 'douban' }
#     , { id: 'UA-7019765-19', namespace: '' }
#     ]
#   , gaInit = function(account) {
#       gaWithNamespace(function(method) {
#         gaInitFn.call(this, method, account)
#       }, account.namespace)
#     }
#   , gaInitFn = function(method, account) {
#       _gaq.push([method('_setAccount'), account.id]);
#       _gaq.push([method('_setSampleRate'), '5']);
#
#
#   _gaq.push([method('_addOrganic'), 'google', 'q'])
#   _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
#   _gaq.push([method('_addOrganic'), 'soso', 'w'])
#   _gaq.push([method('_addOrganic'), 'youdao', 'q'])
#   _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
#   _gaq.push([method('_addOrganic'), 'sogou', 'query'])
#   if (account.namespace) {
#     _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
#     _gaq.push([method('_addIgnoredOrganic'), 'douban'])
#     _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
#     _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
#   }
#
#       if (account.namespace === 'douban') {
#         _gaq.push([method('_setDomainName'), '.douban.com'])
#       }
#
#         _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])
#
#         _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);
#
#       _gaq.push([method('_trackPageview')])
#     }
#
# for(var i = 0, l = accounts.length; i < l; i++) {
#   var account = accounts[i]
#   gaInit(account)
# }
#
#
# ;(function() {
#     var ga = document.createElement('script');
#     ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
#     ga.setAttribute('async', 'true');
#     document.documentElement.firstChild.appendChild(ga);
# })()
# </script>
#
#
#
#
#
#
#
#
#
#
#
#     <!-- daisy2b-docker-->
#
#   <script>_SPLITTEST=''</script>
# </body>
#
# </html>
# '''
# soup = BeautifulSoup(content, "html.parser")
# text = soup.find_all('p', class_='comment-con')

# print soup.div.has_attr('class')

# for s in text:
#     if s.string!=None:
#         print s.string



#jd评论
# page = 1
# while page<=5:
#     print page
#     res = requests.get('https://sclub.jd.com/comment/productPageComments.action?productId=5089239&score=0&sortType=5&page='+str(page)+'&pageSize=10&isShadowSku=0&rid=0&fold=1')
#     content = res.text
#     print content
#     xxx = json.loads(content)['comments']
#     print xxx
#     for i in xxx:
#         print i['content'].replace('\n','')
#     page = page + 1
#     print '----------------'


page = 1
while page<=1:
    print page
    res = requests.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page='+str(page))
    print type(res.content)
    print type(res.text)

    content = res.content

    content = content.decode('utf-8')
    soup = BeautifulSoup(content, "html.parser")
    price = soup.find_all('em',text='￥')
    print len(price)
    print price
    # xxx = json.loads(content)['comments']
    # print xxx
    # for i in xxx:
    #     print i['content'].replace('\n','')
    page = page + 1
    print '----------------'

