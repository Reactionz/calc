use warnings;
use Math::Trig;
use Math::Complex;

my $result;
my $fNum;
my $sNum;

$continue = 'y';

sub add {

    my $r = $_[0] + $_[1];
    return $r;
}

sub subtract {
    my $r = $_[0] - $_[1];
    return $r;
}

sub multiply {
    my $r = $_[0] * $_[1];
    return $r;
}

sub divide {
    my $error = 'cannot divide by zero';
    if($_[1] == 0) {
        return $error;
    }
    my $r = $_[0] / $_[1];

    return $r;
}

sub exponent {
    my $r = $_[0] ** $_[1];
    return $r;
}

sub square {
    my $r = $_[0] ** 2;
    return $r;
}

# Addition, Subtraction, Multiplication, Divisiion
# Sine (degrees), Cosine, Tangent
# Exponential, Natural Logarithm, Square Root (sqrt)
# Power of 2 (sq), Decimal Point, Positive To Negative Change (+/-)
# Clear current input (clear), cancel or reset the calculator option

while($continue eq "y") {
    print "-- Operation Choices --\n";
    print "1 - addition\n";
    print "2 - subtraction\n";
    print "3 - multiplication\n";
    print "4 - division\n";
    print "5 - sine (converts to degrees)\n";
    print "6 - cosine (converts to degrees)\n";
    print "7 - tangent (converts to degrees)\n";
    print "8 - Exponential\n";
    print "9 - Natural Logarithm (ln)\n";
    print "10 - Logarithm Base 10 (log)\n";
    print "11 - Power of 2 (sq)\n";
    print "12 - Square Root (sqrt)\n";
    print "13 - Clear \n";
    print "input result to get the previous result or defaults to 0\n";
    print "choose operation to use:\n";
    my $operation = <STDIN>;
    chomp $operation;
    if($operation eq '1') {
        print "enter first number: ";
        $fNum = <STDIN>;
        chomp $fNum;
        if ($fNum eq 'result') {
                $fNum = $result // 0;
        }
        print "enter second number: ";
        $sNum = <STDIN>;
        chomp $sNum;
        $result = add($fNum, $sNum);

        print "$fNum + $sNum = $result\n";

    } elsif ($operation eq '2') {
        print "enter first number: ";
        $fNum = <STDIN>;
        chomp $fNum;
        if ($fNum eq 'result') {
            $fNum = $result // 0;
        }
        print "enter second number: ";
        $sNum = <STDIN>;
        chomp $sNum;
        $result = subtract($fNum, $sNum);

        print "$fNum - $sNum = $result\n";

    } elsif ($operation eq '3') {
        print "enter first number: ";
        $fNum = <STDIN>;
        chomp $fNum;
        if ($fNum eq 'result') {
            $fNum = $result // 0;
        }
        print "enter second number: ";
        $sNum = <STDIN>;
        chomp $sNum;
        $result = multiply($fNum, $sNum);

        print "$fNum x $sNum = $result\n"

    } elsif($operation eq '4') {
        print "enter first number: ";
        $fNum = <STDIN>;
        chomp $fNum;
        if ($fNum eq 'result') {
            $fNum = $result // 0;
        }
        print "enter second number: ";
        $sNum = <STDIN>;
        chomp $sNum;
        
        $result = divide($fNum, $sNum);

        print "$fNum / $sNum = $result\n"

    } elsif ($operation eq '5') {
        print "enter a number: ";
        $num = <STDIN>;
        chomp $num;
        if ($num eq 'result') {
            $num = $result // 0;
        }
        $result = sin($num * pi / 180);

        print "sin($num) = $result\n";

    } elsif ($operation eq '6') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        if ($num eq 'result') {
            $num = $result // 0;
        }
        $result = cos($num * pi / 180);

        print "cos($num) = $result\n";

    } elsif ($operation eq '7') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        if ($num eq 'result') {
            $num = $result // 0;
        }
        
        $result = tan($num * pi / 180);
        if ($num % 90 == 0) {
            $result = "invalid input";
        }
        print "tan($num) = $result\n";

    } elsif ($operation eq '8') {
        print 'enter first number: ';
        $fNum = <STDIN>;
        chomp $fNum;
        if ($fNum eq 'result') {
            $fNum = $result // 0;
        }
        print 'enter second number: ';
        $sNum = <STDIN>;
        chomp $sNum;

        $result = exponent($fNum, $sNum);

        print "$fNum ^ $sNum = $result\n";

    } elsif ($operation eq '9') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        if ($num eq 'result') {
            $num = $result // 0;
        }
        $result = ln($num);

        print "ln($num) = $result\n";

    } elsif ($operation eq '10') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        if ($num eq 'result') {
            $num = $result // 0;
        }
        $result = log10($num);

        print "log10($num) = $result\n";

    } elsif ($operation eq '11') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        if ($num eq 'result') {
            $num = $result // 0;
        }
        $result = square($num);

        print "sq($num) = $result\n";

    } elsif ($operation eq '12') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        if ($num eq 'result') {
            $num = $result // 0;
        }
        $result = sqrt($num);

        print "sqrt($num) = $result\n";
    } elsif($operation eq '13') {
        print "clearing result\n";
        $result = 0;
    }
    else {
        print 'invalid operation\n'
    }
    print "Would you like to Continue? y/n?\n";
    $continue = <STDIN>;
    chomp $continue;
}
