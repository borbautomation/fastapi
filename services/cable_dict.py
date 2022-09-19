import sympy

s_cable = {
	"14_awg": sympy.Interval(0,2.08),
	"12_awg": sympy.Interval(2.08,3.31),
	"10_awg": sympy.Interval(3.31,5.26),
	"8_awg": sympy.Interval(5.26,8.37),
	"6_awg": sympy.Interval(8.37,13.3),
	"4_awg": sympy.Interval(13.3,21.2),
	"2_awg": sympy.Interval(21.2,33.6),
	"1/0_awg": sympy.Interval(33.6,53.5),
	"2/0_awg": sympy.Interval(53.5,67.4),
	"3/0_awg": sympy.Interval(67.4,85),
	"4/0_awg": sympy.Interval(85,107),
	"250_kcm": sympy.Interval(107,126.7),
	"350_kcm": sympy.Interval(126.7,177.3),
	"400_kcm": sympy.Interval(177.3,203),
	"500_kcm": sympy.Interval(203,253),
	"600_kcm": sympy.Interval(253,304),
	"750_kcm": sympy.Interval(304,380),
	"900_kcm": sympy.Interval(380,456),
	"1000_kcm": sympy.Interval(456,507),
}

gnd_dict_cu = {
	"14_awg": sympy.Interval(0,15),
	"12_awg": sympy.Interval(15,20),
	"10_awg": sympy.Interval(20,60),
	"8_awg": sympy.Interval(60,100),
	"6_awg": sympy.Interval(100,200),
	"4_awg": sympy.Interval(200,300),
	"2_awg": sympy.Interval(300,500),
	"1/0_awg": sympy.Interval(500,800),
	"2/0_awg": sympy.Interval(800,1000),
}

gnd_dict_al = {
	"12_awg": sympy.Interval(0,15),
	"10_awg": sympy.Interval(15,20),
	"8_awg": sympy.Interval(20,60),
	"6_awg": sympy.Interval(60,100),
	"4_awg": sympy.Interval(100,200),
	"2_awg": sympy.Interval(200,300),
	"1/0_awg": sympy.Interval(300,500),
	"2/0_awg": sympy.Interval(500,600),
	"3/0_awg": sympy.Interval(600,800),
	"4/0_awg": sympy.Interval(800,1000),

}