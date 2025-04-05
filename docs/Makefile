SHELL = bash
pub:
	@git commit -am save
	@git push
	@git status

../%.html : %.md
	@sh header.html "`gawk 'sub(/^# /,"")' $^`" > $@ 
	@gawk -f code.awk $^ | python3 markup.py >> $@
