print("start")
io.stdout:write('start ' .. gameinfo.getromname() .. '\n')

i = 0
buttons = {}
while true do
	if i > 10 then
		temp = io.stdin:read("*a")
		loadstring(temp)()
		io.stdout:write("\n")
	else
		i = i + 1
		emu.frameadvance()
	end
end
