#!/usr/bin/perl

use strict;
use warnings;

my $delim = shift @ARGV || "/";
my $mode  = shift @ARGV || "w";

while (<STDIN>) {
    chomp;
    my @tokens = split(/\s+/, $_);
    foreach my $token (@tokens) {
        my @parts = split(/\Q$delim\E/, $token);
        if (@parts >= 2) {
            my $tag = pop @parts;
            my $word = join($delim, @parts);
            if ($mode eq "w") {
                print "$word\t$tag\n";
            } elsif ($mode eq "c") {
                my @chars = split(//, $word);
                for (my $i=0; $i<=$#chars; $i++) {
                    my $bio = ($i == 0) ? "B" : "I";
                    print "$chars[$i]\t$bio-$tag\n";
                }
            }
        }
    }
    print "\n";
}
