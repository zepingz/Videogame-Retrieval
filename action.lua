function memory(path)
	local f = io.open(path, "wb")
	ram = mainmemory.readbyterange(0, 4096)
	for key, value in pairs(ram) do
		f:write(string.char(value))
	end
	f:close()
end

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
