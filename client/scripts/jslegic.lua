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

	-- Read the parameters
	for o, a in getopt.getopt(args, 'h') do
		if o == "h" then help() return end
	end
	
	local _cmds = {
    --[[
    --]]
	[0] = "hf legic reader",
	[1] = "data hexsamples 256",
	}
	core.clearCommandBuffer()
	
	--local i
	--for _,c in pairs(_cmds) do 
	
	core.console( _cmds[0] )
	core.console( _cmds[1] )
	
end

main(args)
