echo "Content-type: text/html"
echo ""
[ "$QUERY_STRING" == "reset" ] && git pull
