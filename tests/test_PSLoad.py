# -*- coding: utf-8 -*-
import psst.cli as p

try:
    p.scuc(
        "C:/Users/huan289/Qiuhua/FY2016_Project_Transactive_system/ERCOTTestSystem/AMES-V5.0/DATA/PSST_TestCases/case8ReferenceModel_1PSL.dat",
        "C:/Users/huan289/Qiuhua/FY2016_Project_Transactive_system/ERCOTTestSystem/AMES-V5.0/psst/tests/GenCoSchedule.dat",
        "cbc",
    )
except:
    pass
