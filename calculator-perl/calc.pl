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
    print "choose operation to use:\n";
    print "1 - addition\n";
    print "2 - subtraction\n";
    print "3 - multiplication\n";
    print "4 - division\n";
    print "5 - sine\n";
    print "6 - cosine\n";
    print "7 - tangent\n";
    print "8 - Exponential\n";
    print "9 - Natural Logarithm (ln)\n";
    print "10 - Logarithm Base 10 (log)\n";
    print "11 - Power of 2 (sq)\n";
    print "12 - Square Root (sqrt)\n";

    my $operation = <STDIN>;
    chomp $operation;
    
    if($operation eq '1') {
        print "enter first number: ";
        $fNum = <STDIN>;
        chomp $fNum;
        print "enter second number: ";
        $sNum = <STDIN>;
        chomp $sNum;
        $result = add($fNum, $sNum);

        print "$fNum + $sNum = $result\n";

    } elsif ($operation eq '2') {
        print "enter first number: ";
        $fNum = <STDIN>;
        chomp $fNum;
        print "enter second number: ";
        $sNum = <STDIN>;
        chomp $sNum;
        $result = subtract($fNum, $sNum);

        print "$fNum - $sNum = $result\n";

    } elsif ($operation eq '3') {
        print "enter first number: ";
        $fNum = <STDIN>;
        chomp $fNum;
        print "enter second number: ";
        $sNum = <STDIN>;
        chomp $sNum;
        $result = multiply($fNum, $sNum);

        print "$fNum x $sNum = $result\n"

    } elsif($operation eq '4') {
        print "enter first number: ";
        $fNum = <STDIN>;
        chomp $fNum;
        print "enter second number: ";
        $sNum = <STDIN>;
        chomp $sNum;
        $result = divide($fNum, $sNum);

        print "$fNum / $sNum = $result\n"

    } elsif ($operation eq '5') {
        print "enter a number: ";
        $num = <STDIN>;
        chomp $num;
        $result = sin($num * pi / 180);

        print "sin($num) = $result\n";

    } elsif ($operation eq '6') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        $result = cos($num * pi / 180);

        print "cos($num) = $result\n";

    } elsif ($operation eq '7') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        $result = tan($num * pi / 180);

        print "tan($num) = $result\n";

    } elsif ($operation eq '8') {
        print 'enter first number: ';
        $fNum = <STDIN>;
        chomp $fNum;
        print 'enter second number: ';
        $sNum = <STDIN>;
        chomp $sNum;

        $result = exponent($fNum, $sNum);

        print "$fNum ^ $sNum = $result\n";

    } elsif ($operation eq '9') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        $result = ln($num);

        print "ln($num) = $result\n";

    } elsif ($operation eq '10') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        $result = log10($num);

        print "log10($num) = $result\n";

    } elsif ($operation eq '11') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        $result = square($num);

        print "sq($num) = $result\n";

    } elsif ($operation eq '12') {
        print 'enter a number: ';
        $num = <STDIN>;
        chomp $num;
        $result = sqrt($num);

        print "sqrt($num) = $result\n";
    } else {
        print 'invalid operation'
    }
    print "Would you like to Continue? y/n?\n";
    $continue = <STDIN>;
    chomp $continue;
}