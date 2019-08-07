rm program
gcc -o program /home/pi/RugratsC/*.c
echo "Compilado"
if [ -f program ]
then
	sudo valgrind --leak-check=yes ./program tx
fi