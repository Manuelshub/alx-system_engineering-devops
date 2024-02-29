#!/usr/bin/env ruby
# The Script should print: [SENDER],[RECEIVER],[FLAGS]
# The sender phone numbr or name(including country code if present)
# The receiver phone numberor name
# The flags that were used.
puts ARGV[0].scan(/\[from:(\+?\w+)\] \[to:(\+?\w+)\] \[flags:(-?\d:-?\d:-?\d:-?\d:-?\d)\]/).join(",")
