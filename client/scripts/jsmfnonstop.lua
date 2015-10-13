local getopt = require('getopt')

example = "script run jsmfnonstop"
author = "Stoye"

desc =
[[
This is a script for doing multiple rounds of hf mf nested command without saving the result.

Arguments:
	-h 		this help
	-n      number of rounds to do hfmfnested
]]
--- 
-- A debug printout-function
function dbg(args)
	if DEBUG then
		print("###", args)
	end
end 
--- 
-- This is only meant to be used when errors occur
function oops(err)
	print("ERROR: ",err)
end

--- 
-- Usage help
function help()
	print(desc)
	print("Example usage")
	print(example)
end

--- 
-- The main entry point
function main(args)

	local num = 20
	-- Read the parameters
	for o, a in getopt.getopt(args, 'hn:') do
		if o == "h" then help() return end
		if o == "n" then num=a-1 end
	end
	
	local _cmds = {
    --[[
    --]]
	[0] = "hf mf nested 1 0 A a0a1a2a3a4a5",
	[1] = "hf 14a raw -p -a 43",
	[2] = "hf 14a raw -c -p -a A000",
	[3] = "hf 14a raw -c -p -a 01 02 03 04 04 98 02 00 00 00 00 00 00 00 10 01",
	}
	core.clearCommandBuffer()
	
	local i
	--for _,c in pairs(_cmds) do 
	
	for i = 0, num do
	    print ( "Runde "..(i+1) )
		core.console( _cmds[0] )
	end
end

main(args)
