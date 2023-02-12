BEGIN {
     Color1="DarkBlue"
     Color2="teal"  
     Color3="f79a32"
     Color4="brown" 
     Words="and break do else elseif end false "\
   	   "for function if in local nil not or "\
	   "repeat return then true until while require dofile"
     split(Words,Tmp," ")
     for(Word in Tmp) {
        Pat = Pat Sep "\\y" Tmp[Word] "\\y"
        Sep = "|"
     }
     Pat = "(" Pat ")"
     In = 0
}
!In &&/```/  { In=1; print("<pre><code>")  ; next }
In  && /```/ { In=0; print("</pre></code>"); next }
             { print(In ? pretty($0) : $0)        }

function pretty(str) { 
  gsub(/[\+=\*-/<>^{}\[\]]/, "<font color=gray><b>&</b></font>",str)
  gsub(/<[\/]?code>/,"",str)
  gsub(Pat,          "<font color="Color1"><b>&</b></font>",str) 
  gsub(/"[^"]*"/,    "<font color="Color2">&</font>",str)
  gsub(/#.*/,        "<font color="Color3">&</font>",str)
  str = gensub(/(\y[_a-zA-Z0-9]+\y)\(/, "<font color="Color4">\\1</font>(","g",str)
  return str
}

