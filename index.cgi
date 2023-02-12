#!/bin/bash
# vim: set ts=2 sw=2 et : 
# -*- bash -*- 
########################################################
# begin config section

Default=index
Src=${Src='https://raw.githubusercontent.com/timm/smell101/main/README.md'}
Cat=${Cat=" wget -q -O - $Src"}
Files='index.cgi'
Tmp=/tmp/$USER

header() { cat<<-EOF
<!DOCTYPE html>
<html>
<head>
    <title> $2 : 101 bad smells </title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta charset="UTF-8" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/languages/lua.min.js"></script>
    <script>hljs.highlightAll();</script>
    <script type="text/javascript" async 
	              src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-MML-AM_CHTML">
    </script>
    <style>
     body {
       font-family: Optima, Segoe, "Segoe UI", Candara, Calibri, Arial, sans-serif; 
       line-height: 1.4;
       max-width: 38rem;
       padding: 2rem;
       margin: auto;
      }
     img.right200 { width: 200px; border:1px solid #999; padding:3px; margin:5px; float:right; }
     .top ul {list-style: none;padding: 0px;margin: 0px;}
     .top ul li {display: block;position: relative;float: left;border:1px solid #000}
     .top li ul {display: none;}
     .top ul li a {display: block;background: #000;padding: 5px 10px 5px 10px;text-decoration: none; 
                  white-space: nowrap;color: #fff;}
     .top ul li a:hover {background: #808080;}
     .top li:hover ul {display: block; position: absolute;}
     .top li:hover li {float: none;}
     .top li:hover a {background: #808080;}
     .top li:hover li a:hover {background: #000;}
     .top #drop-nav li ul li {border-top: 0px;}
    </style>
</head>
<body>
  <small>$1 &nbsp; <a href="#">&copy; 2023</a> by <a href="#">timm</a><br>
  <div class="top">
     <ul id="drop-nav">
      <li><a href="#">Home</a></li>
      <li><a href="https://github.com/timm/lua">Code </a></li>
      <ul>
        <li><a href="#">HTML</a></li>
        <li><a href="#">CSS</a></li>
        <li><a href="#">JavaScript</a></li>
      </ul>
      <li><a href="#">Content </a>
        <ul>
          <li><a href="#">Joomla</a></li>
          <li><a href="#">Drupal</a></li>
          <li><a href="#">WordPress</a></li>
          <li><a href="#">Concrete 5</a></li>
        </ul>
      </li>
      <li><a href="#">Contact</a>
        <ul>
          <li><a href="#">Inquiries</a></li>
          <li><a href="#">Questions</a></li>
        </ul>
      </li>
    </ul>
    </small> </div> <br clear=all>

EOF
}

# from here down, you should not need to change anything
[ -n "$1" ] && QUERY_STRING=$1

Q=${QUERY_STRING:=$Default}
Q=$(echo $Q | sed 's/[^\/\.0-9a-zA-Z]//g')
  
echo "Content-type: text/html"
echo ""
header $Q asdsadas 
echo "</body></html>"