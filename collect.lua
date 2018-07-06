io.stdout:write('start ' .. gameinfo.getromname() .. '\n')
interval = io.stdin:read("*a")
path = "data\\" .. gameinfo.getromname() .. "\\"
os.execute("mkdir " .. "data\\\"" .. gameinfo.getromname() .. "\"\\" .. "states")
savestate.save(path .. "root.state")
end_frame = movie.length()
client.speedmode(400)

for frame = 0, end_frame do
	if frame % interval == 0 then --and frame ~= 0 then
		client.screenshot(path .. "\\screenshots\\" .. frame .. ".png")
		f = io.open(path .. "\\states\\" .. frame .. ".bin", "wb")
		ram = mainmemory.readbyterange(0, mainmemory.getcurrentmemorydomainsize())
		for key, value in pairs(ram) do
			f:write(string.char(value))
		end
		f:close()
	end
	emu.frameadvance()
end
client.exit()