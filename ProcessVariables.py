"""Master variable file"""
directory_of_files_to_process_TESTING = r"E:\DoIT_SDATRealProperty_Project\RealPropAllData\DataForTesting"
# timestamp
GOOGLE_ROOT_URL = (r"",)
GOOGLE_URL_QUERYSTRING_PARAMETER_SEPARATOR = (",",)
GOOGLE_URL_QUERY_PARAMETER_CONCATENATE_SYMBOL = ("+",)
FINDERONLINE_ROOT_URL = (r"",)
URL_ENCODING_SPACE = ("%20",)
MARYLAND_ABBREVIATION = ("MD",)
SOURCE_COORDINATE_SYSTEM_EPSG = (26985,)
DESTINATION_COORDINATE_SYSTE_EPSG = (4326,)
BLANK_STRING = ("",)
SDAT_DATA_SPLIT_SPACE_DELIMITED_INDICES = (
2, 2, 12, 2, 2, 1, 34, 34, 25, 30, 30, 22, 2, 5, 4, 4, 20, 24, 24, 5, 1, 2, 22, 5, 22, 5, 4, 6, 3, 5, 4, 3, 5, 4, 1, 3,
4, 6, 3, 5, 5, 5, 5, 5, 5, 1, 1, 1, 3, 2, 1, 1, 4, 4, 1, 6, 2, 2, 2, 1, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 3,
2, 2, 6, 34, 3, 5, 4, 3, 5, 4, 1, 1, 8, 9, 1, 9, 5, 1, 9, 9, 2, 12, 6, 34, 3, 5, 4, 3, 5, 4, 1, 1, 8, 9, 1, 9, 5, 1, 9,
9, 2, 12, 6, 34, 3, 5, 4, 3, 5, 4, 1, 1, 8, 9, 1, 9, 5, 1, 9, 9, 2, 12, 3, 9, 4, 3, 9, 4, 3, 9, 4, 9, 4, 9, 4, 9, 4, 9,
9, 9, 9, 6, 6, 4, 9, 9, 9, 9, 9, 9, 9, 6, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 4, 40, 8, 9, 9, 9,
1, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 1, 8, 8, 8, 8, 8, 10, 1, 8, 9, 8, 8, 10, 1, 8, 8, 2, 8, 8, 8, 8, 8, 1, 1, 2, 2, 1,
2, 4, 5, 5, 1, 4, 2, 7, 12, 1, 8, 8, 4, 9, 9, 9, 9, 9, 9, 7, 7, 7, 1, 8, 150, 1, 8, 3, 3, 3, 4, 4, 2, 7, 4, 18, 2, 12,
6, 3, 1, 8, 1, 8, 1, 8, 8, 8, 4, 1, 1)
SDAT_TO_MDP_DATA_FILES_MAPPING = (('PublicData_01.txt', 'ALLE.csv'),
                                  ('PublicData_02.txt', 'ANNE.csv'),
                                  ('PublicData_03.txt', 'BACI.csv'),
                                  ('PublicData_04.txt', 'BACO.csv'),
                                  ('PublicData_05.txt', 'CALV.csv'),
                                  ('PublicData_06.txt', 'CARO.csv'),
                                  ('PublicData_07.txt', 'CARR.csv'),
                                  ('PublicData_08.txt', 'CECI.csv'),
                                  ('PublicData_09.txt', 'CHAR.csv'),
                                  ('PublicData_10.txt', 'DORC.csv'),
                                  ('PublicData_11.txt', 'FRED.csv'),
                                  ('PublicData_12.txt', 'GARR.csv'),
                                  ('PublicData_13.txt', 'HARF.csv'),
                                  ('PublicData_14.txt', 'HOWA.csv'),
                                  ('PublicData_15.txt', 'KENT.csv'),
                                  ('PublicData_16.txt', 'MONT.csv'),
                                  ('PublicData_17.txt', 'PRIN.csv'),
                                  ('PublicData_18.txt', 'QUEE.csv'),
                                  ('PublicData_19.txt', 'STMA.csv'),
                                  ('PublicData_20.txt', 'SOME.csv'),
                                  ('PublicData_21.txt', 'TALB.csv'),
                                  ('PublicData_22.txt', 'WASH.csv'),
                                  ('PublicData_23.txt', 'WICO.csv'),
                                  ('PublicData_24.txt', 'WORC.csv'),
                                  )
COUNTY_CODE_DIGIT_TO_CHAR_VALUES = (('01', 'ALLE'),
                              ('02', 'ANNE'),
                              ('03', 'BACI'),
                              ('04', 'BACO'),
                              ('05', 'CALV'),
                              ('06', 'CARO'),
                              ('07', 'CARR'),
                              ('08', 'CECI'),
                              ('09', 'CHAR'),
                              ('10', 'DORC'),
                              ('11', 'FRED'),
                              ('12', 'GARR'),
                              ('13', 'HARF'),
                              ('14', 'HOWA'),
                              ('15', 'KENT'),
                              ('16', 'MONT'),
                              ('17', 'PRIN'),
                              ('18', 'QUEE'),
                              ('19', 'STMA'),
                              ('20', 'SOME'),
                              ('21', 'TALB'),
                              ('22', 'WASH'),
                              ('23', 'WICO'),
                              ('24', 'WORC'),
                              )
COUNTY_CODE_TO_COUNTY_NAME = (("01", "Allegany"),
                              ("02", "Anne Arundel"),
                              ("03", "Baltimore City"),
                              ("04", "Baltimore County"),
                              ("05", "Calvert"),
                              ("06", "Caroline"),
                              ("07", "Carroll"),
                              ("08", "Cecil"),
                              ("09", "Charles"),
                              ("10", "Dorchester"),
                              ("11", "Frederick"),
                              ("12", "Garrett"),
                              ("13", "Harford"),
                              ("14", "Howard"),
                              ("15", "Kent"),
                              ("16", "Montgomery"),
                              ("17", "Prince George's"),
                              ("18", "Queen Anne's"),
                              ("19", "St. Mary's"),
                              ("20", "Somerset"),
                              ("21", "Talbot"),
                              ("22", "Washington"),
                              ("23", "Wicomico"),
                              ("24", "Worcester"),
                              )
DWELLING_STORY_TO_VALUE = (('0001', 'STRY 1 Story No Basement (0001)'),
                           ('0002', 'STRY 1 Story With Basement (0002)'),
                           ('0003', 'STRY 1 1/2 Story No Basement (0003)'),
                           ('0004', 'STRY 1 1/2 Story With Basement (0004)'),
                           ('0005', 'STRY 2 Story No Basement (0005)'),
                           ('0006', 'STRY 2 Story With Basement (0006)'),
                           ('0007', 'STRY 2 1/2 Story No Basement (0007)'),
                           ('0008', 'STRY 2 1/2 Story With Basement (0008)'),
                           ('0009', 'STRY 3 Story No Basement (0009)'),
                           ('0010', 'STRY 3 Story With Basement (0010)'),
                           ('0011', 'STRY 4 Story No Basement (0011)'),
                           ('0012', 'STRY 4 Story With Basement (0012)'),
                           ('0013', 'STRY Split Foyer (0013)'),
                           ('0015', 'STRY TH End 1 Story No Basement (0015)'),
                           ('0016', 'STRY TH End 1 Story With Basement (0016)'),
                           ('0017', 'STRY TH End 1 1/2 Story No Basement (0017)'),
                           ('0018', 'STRY TH End 1 1/2 Story With Basement (0018)'),
                           ('0019', 'STRY TH End 2 Story No Basement (0019)'),
                           ('0020', 'STRY TH End 2 Story With Basement (0020)'),
                           ('0021', 'STRY TH End 2 1/2 Story No Basement (0021)'),
                           ('0022', 'STRY TH End 2 1/2 Story With Basement (0022)'),
                           ('0023', 'STRY TH End 3 Story No Basement (0023)'),
                           ('0024', 'STRY TH End 3 Story With Basement (0024)'),
                           ('0025', 'STRY TH End 4 Story No Basement (0025)'),
                           ('0026', 'STRY TH End 4 Story With Basement (0026)'),
                           ('0027', 'STRY TH End Split Foyer (0027)'),
                           ('0029', 'STRY TH Center 1 Story No Basement (0029)'),
                           ('0030', 'STRY TH Center 1 Story With Basement (0030)'),
                           ('0031', 'STRY TH Center 1 1/2 Story No Basement (0031)'),
                           ('0032', 'STRY TH Center 1 1/2 Story With Basement (0032)'),
                           ('0033', 'STRY TH Center 2 Story No Basement (0033)'),
                           ('0034', 'STRY TH Center 2 Story With Basement (0034)'),
                           ('0035', 'STRY TH Center 2 1/2 Story No Basement (0035)'),
                           ('0036', 'STRY TH Center 2 1/2 Story With Basement (0036)'),
                           ('0037', 'STRY TH Center 3 Story No Basement (0037)'),
                           ('0038', 'STRY TH Center 3 Story With Basement (0038)'),
                           ('0039', 'STRY TH Center 4 Story No Basement (0039)'),
                           ('0040', 'STRY TH Center 4 Story With Basement (0040)'),
                           ('0041', 'STRY TH Center Split Foyer (0041)'),
                           ('C101', 'HOUSING Apartment(s) (C101)'),
                           ('C102', 'REC City Club (C102)'),
                           ('C103', 'SCHOOL Building Dormitory (C103)'),
                           ('C104', 'TRAVEL Hotel (C104)'),
                           ('C105', 'CARE Home for the Elderly (C105)'),
                           ('C106', 'REC Club House (C106)'),
                           ('C107', 'REC Health Club (C107)'),
                           ('C108', 'REC Country Club (C108)'),
                           ('C109', 'BURIAL Mortuary (C109)'),
                           ('C110', 'CARE Group Home (C110)'),
                           ('C111', 'COMMUNITY Rectory (C111)'),
                           ('C112', 'TRAVEL Motel (C112)'),
                           ('C113', 'HOUSING Residence Multiple (C113)'),
                           ('C114', 'STORE Department (C114)'),
                           ('C115', 'STORE Retail (C115)'),
                           ('C116', 'STORE Discount (C116)'),
                           ('C117', 'STORE Beauty and/or Barber Shop (C117)'),
                           ('C118', 'STORE Laundromat (C118)'),
                           ('C119', 'STORE Shopping Center Regional (C119)'),
                           ('C120', 'STORE Shopping Center Community (C120)'),
                           ('C121', 'STORE Shopping Center Neighborhood (C121)'),
                           ('C122', 'SAFETY Armory (C122)'),
                           ('C123', 'INDUSTRY Engineering and Research (C123)'),
                           ('C124', 'INDUSTRY Light Manufacturing (C124)'),
                           ('C125', 'WAREHOUSE Distribution (C125)'),
                           ('C126', 'WAREHOUSE Storage (C126)'),
                           ('C127', 'WAREHOUSE Transit (C127)'),
                           ('C128', 'WAREHOUSE Mini Storage (C128)'),
                           ('C129', 'TRANSPORT Hangar (C129)'),
                           ('C130', 'TRANSPORT Hangar T Hangar (C130)'),
                           ('C131', 'COMMUNITY Post Office Main (C131)'),
                           ('C132', 'AUTO Service Garage (C132)'),
                           ('C133', 'AUTO Service Storage Garage (C133)'),
                           ('C134', 'AUTO Service Mini Lube (C134)'),
                           ('C135', 'AUTO Auto Center (C135)'),
                           ('C136', 'AUTO Auto Showroom (C136)'),
                           ('C137', 'AUTO Parking Structure (C137)'),
                           ('C138', 'OFFICE Building (C138)'),
                           ('C139', 'OFFICE Building Medical (C139)'),
                           ('C140', 'PUBLIC Government Building (C140)'),
                           ('C141', 'CARE Hospital General (C141)'),
                           ('C142', 'CARE Surgical Center (C142)'),
                           ('C143', 'CARE Hospital Convalescent (C143)'),
                           ('C144', 'CARE Dispensary (C144)'),
                           ('C145', 'SAFETY Jail (C145)'),
                           ('C146', 'OFFICE Veterinary Hospital (C146)'),
                           ('C147', 'SAFETY Fire Station (C147)'),
                           ('C148', 'COMMUNITY Library (C148)'),
                           ('C149', 'BANK Bank Branch (C149)'),
                           ('C150', 'SCHOOL Elementary (C150)'),
                           ('C151', 'SCHOOL Building Classroom (C151)'),
                           ('C152', 'SCHOOL Building Multi-Purpose School (C152)'),
                           ('C153', 'SCHOOL Building Manual Arts (C153)'),
                           ('C154', 'COMMUNITY Building Restroom (C154)'),
                           ('C155', 'COMMUNITY Building Shower (C155)'),
                           ('C156', 'REC Gymnasium (C156)'),
                           ('C157', 'CARE Day Care Center (C157)'),
                           ('C158', 'COMMUNITY Church (C158)'),
                           ('C159', 'REC Auditorium (C159)'),
                           ('C160', 'REC Fraternal Building (C160)'),
                           ('C161', 'REC Cinema (C161)'),
                           ('C162', 'REC Skating Rink (C162)'),
                           ('C163', 'REC Handball and/or Racquetball Court(s) (C163)'),
                           ('C164', 'REC Bowling Alley (C164)'),
                           ('C165', 'REC Tennis Facility Indoor (C165)'),
                           ('C166', 'RESTAURANT (C166)'),
                           ('C167', 'RESTAURANT Fast Food (C167)'),
                           ('C168', 'STORE Convenience (C168)'),
                           ('C169', 'STORE Market (C169)'),
                           ('C170', 'STORE Dairy (C170)'),
                           ('C171', 'STORE Mall Enclosed (C171)'),
                           ('C172', 'STORE Mall Covered (C172)'),
                           ('C173', 'STORE Mall Open (C173)'),
                           ('C174', 'INDUSTRY Industrial Heavy (C174)'),
                           ('C175', 'WAREHOUSE Cold Storage Facility (C175)'),
                           ('C176', 'SCHOOL Building Fraternity House (C176)'),
                           ('C177', 'SAFETY Fire Station Volunteer (C177)'),
                           ('C178', 'WAREHOUSE Discount (C178)'),
                           ('C179', 'HOUSING Residential/Retail Mixed (C179)'),
                           ('C180', 'STORE Shopping Center Regional Shell (C180)'),
                           ('C181', 'STORE Shopping Center Community Shell (C181)'),
                           ('C182', 'STORE Shopping Center Neighborhood Shell (C182)'),
                           ('C183', 'STORE Shopping Center Regional Finished (C183)'),
                           ('C184', 'STORE Shopping Center Neighborhood Finished (C184)'),
                           ('C185', 'INDUSTRY Flex Space (C185)'),
                           ('C186', 'TRANSPORT Hangar Storage (C186)'),
                           ('C187', 'AUTO Auto Dealership Complete (C187)'),
                           ('C188', 'INDUSTRY Industrial Shell (C188)'),
                           ('C189', 'INDUSTRY Industrial Finished (C189)'),
                           ('C190', 'INDUSTRY Loft (C190)'),
                           ('C191', 'AUTO Service Station (C191)'),
                           ('C192', 'RESTAURANT Food Booth (C192)'),
                           ('C193', 'REC Theater (C193)'),
                           ('C194', 'SCHOOL High (C194)'),
                           ('C195', 'SCHOOL Building Laboratory (C195)'),
                           ('C196', 'SCHOOL Building Computer Center (C196)'),
                           ('C197', 'COMMUNITY Post Office Branch (C197)'),
                           ('C198', 'WAREHOUSE Mega (C198)'),
                           ('C199', 'CARE Dental Clinic (C199)'),
                           ('C200', 'BANK Bank Main (C200)'),
                           ('C201', 'BANK Bank Mini (C201)'),
                           ('C202', 'TRANSPORT Passenger Terminal (C202)'),
                           ('C203', 'RESTAURANT Tavern (C203)'),
                           ('C204', 'WAREHOUSE Mini Storage Multi Story (C204)'),
                           ('C225', 'OTHER Condominium Non-Residential (C225)'),
                           ('C226', 'OTHER Special Use (C226)'),
                           ('C227', 'HOUSING Residence (C227)'),
                           ('C301', 'OFFICE Building Condominium (C301)'),
                           ('C302', 'WAREHOUSE Condominium (C302)'),
                           ('C303', 'STORE Retail Condominium (C303)'),
                           ('C304', 'BOAT Marina Condominium Slip (C304)'),
                           ('C305', 'OTHER Building Per Square Foot (C305)'),
                           ('C306', 'OTHER Building Per Unit (C306)'),
                           ('C307', 'HOUSING Residential Apartment Unit(s) (C307)'),
                           ('C308', 'HOUSING Rental Townhouse Unit(s) (C308)'),
                           ('C309', 'HOUSING Efficiency/Efficiencies (C309)'),
                           ('C310', 'HOUSING 1 Bedroom (C310)'),
                           ('C311', 'HOUSING 2 Bedrooms (C311)'),
                           ('C312', 'HOUSING 3 Bedrooms (C312)'),
                           ('C313', 'HOUSING 4 Bedrooms (C313)'),
                           ('C314', 'AUTO Parking Space (C314)'),
                           ('CND', 'HOUSING Condominium(s) (CND)'),
                           ('MH1', 'HOUSING Mobile Home(s) (MH1)'),
                           )
DWELLING_TYPE_TO_VALUE = (('00001', 'DWEL Standard Unit (0001)'),
                          ('00002', 'DWEL End Unit (0002)'),
                          ('00003', 'DWEL Center Unit (0003)'),
                          ('00004', 'DWEL Split Foyer (0004)'),
                          ('00005', 'DWEL Split Level (0005)'),
                          ('00006', 'DWEL Mobile Home (0006)'),
                          ('00007', 'DWEL Condominium Townhouse (0007)'),
                          ('00008', 'DWEL Condominium Garden Unit (0008)'),
                          ('00009', 'DWEL Condominium High Rise (0009)'),
                          ('00010', 'DWEL Condominium Penthouse (0010)'),
                          ('00011', 'DWEL Condominium Studio (0011)'),
                          ('00012', 'DWEL Boat Slip (0012)'),
                          ('00013', 'DWEL Rental Dwelling (0013)'),
                          ('00014', 'DWEL Parking Space (0014)'),
                          ('00015', 'DWEL Storage Unit (0015)'),
                          ('C101', 'HOUSING Apartment(s) (C101)'),
                          ('C102', 'REC City Club (C102)'),
                          ('C103', 'SCHOOL Building Dormitory (C103)'),
                          ('C104', 'TRAVEL Hotel (C104)'),
                          ('C105', 'CARE Home for the Elderly (C105)'),
                          ('C106', 'REC Club House (C106)'),
                          ('C107', 'REC Health Club (C107)'),
                          ('C108', 'REC Country Club (C108)'),
                          ('C109', 'BURIAL Mortuary (C109)'),
                          ('C110', 'CARE Group Home (C110)'),
                          ('C111', 'COMMUNITY Rectory (C111)'),
                          ('C112', 'TRAVEL Motel (C112)'),
                          ('C113', 'HOUSING Residence Multiple (C113)'),
                          ('C114', 'STORE Department (C114)'),
                          ('C115', 'STORE Retail (C115)'),
                          ('C116', 'STORE Discount (C116)'),
                          ('C117', 'STORE Beauty and/or Barber Shop (C117)'),
                          ('C118', 'STORE Laundromat (C118)'),
                          ('C119', 'STORE Shopping Center Regional (C119)'),
                          ('C120', 'STORE Shopping Center Community (C120)'),
                          ('C121', 'STORE Shopping Center Neighborhood (C121)'),
                          ('C122', 'SAFETY Armory (C122)'),
                          ('C123', 'INDUSTRY Engineering and Research (C123)'),
                          ('C124', 'INDUSTRY Light Manufacturing (C124)'),
                          ('C125', 'WAREHOUSE Distribution (C125)'),
                          ('C126', 'WAREHOUSE Storage (C126)'),
                          ('C127', 'WAREHOUSE Transit (C127)'),
                          ('C128', 'WAREHOUSE Mini Storage (C128)'),
                          ('C129', 'TRANSPORT Hangar (C129)'),
                          ('C130', 'TRANSPORT Hangar T Hangar (C130)'),
                          ('C131', 'COMMUNITY Post Office Main (C131)'),
                          ('C132', 'AUTO Service Garage (C132)'),
                          ('C133', 'AUTO Service Storage Garage (C133)'),
                          ('C134', 'AUTO Service Mini Lube (C134)'),
                          ('C135', 'AUTO Auto Center (C135)'),
                          ('C136', 'AUTO Auto Showroom (C136)'),
                          ('C137', 'AUTO Parking Structure (C137)'),
                          ('C138', 'OFFICE Building (C138)'),
                          ('C139', 'OFFICE Building Medical (C139)'),
                          ('C140', 'PUBLIC Government Building (C140)'),
                          ('C141', 'CARE Hospital General (C141)'),
                          ('C142', 'CARE Surgical Center (C142)'),
                          ('C143', 'CARE Hospital Convalescent (C143)'),
                          ('C144', 'CARE Dispensary (C144)'),
                          ('C145', 'SAFETY Jail (C145)'),
                          ('C146', 'OFFICE Veterinary Hospital (C146)'),
                          ('C147', 'SAFETY Fire Station (C147)'),
                          ('C148', 'COMMUNITY Library (C148)'),
                          ('C149', 'BANK Bank Branch (C149)'),
                          ('C150', 'SCHOOL Elementary (C150)'),
                          ('C151', 'SCHOOL Building Classroom (C151)'),
                          ('C152', 'SCHOOL Building Multi-Purpose School (C152)'),
                          ('C153', 'SCHOOL Building Manual Arts (C153)'),
                          ('C154', 'COMMUNITY Building Restroom (C154)'),
                          ('C155', 'COMMUNITY Building Shower (C155)'),
                          ('C156', 'REC Gymnasium (C156)'),
                          ('C157', 'CARE Day Care Center (C157)'),
                          ('C158', 'COMMUNITY Church (C158)'),
                          ('C159', 'REC Auditorium (C159)'),
                          ('C160', 'REC Fraternal Building (C160)'),
                          ('C161', 'REC Cinema (C161)'),
                          ('C162', 'REC Skating Rink (C162)'),
                          ('C163', 'REC Handball and/or Racquetball Court(s) (C163)'),
                          ('C164', 'REC Bowling Alley (C164)'),
                          ('C165', 'REC Tennis Facility Indoor (C165)'),
                          ('C166', 'RESTAURANT (C166)'),
                          ('C167', 'RESTAURANT Fast Food (C167)'),
                          ('C168', 'STORE Convenience (C168)'),
                          ('C169', 'STORE Market (C169)'),
                          ('C170', 'STORE Dairy (C170)'),
                          ('C171', 'STORE Mall Enclosed (C171)'),
                          ('C172', 'STORE Mall Covered (C172)'),
                          ('C173', 'STORE Mall Open (C173)'),
                          ('C174', 'INDUSTRY Industrial Heavy (C174)'),
                          ('C175', 'WAREHOUSE Cold Storage Facility (C175)'),
                          ('C176', 'SCHOOL Building Fraternity House (C176)'),
                          ('C177', 'SAFETY Fire Station Volunteer (C177)'),
                          ('C178', 'WAREHOUSE Discount (C178)'),
                          ('C179', 'HOUSING Residential/Retail Mixed (C179)'),
                          ('C180', 'STORE Shopping Center Regional Shell (C180)'),
                          ('C181', 'STORE Shopping Center Community Shell (C181)'),
                          ('C182', 'STORE Shopping Center Neighborhood Shell (C182)'),
                          ('C183', 'STORE Shopping Center Regional Finished (C183)'),
                          ('C184', 'STORE Shopping Center Neighborhood Finished (C184)'),
                          ('C185', 'INDUSTRY Flex Space (C185)'),
                          ('C186', 'TRANSPORT Hangar Storage (C186)'),
                          ('C187', 'AUTO Auto Dealership Complete (C187)'),
                          ('C188', 'INDUSTRY Industrial Shell (C188)'),
                          ('C189', 'INDUSTRY Industrial Finished (C189)'),
                          ('C190', 'INDUSTRY Loft (C190)'),
                          ('C191', 'AUTO Service Station (C191)'),
                          ('C192', 'RESTAURANT Food Booth (C192)'),
                          ('C193', 'REC Theater (C193)'),
                          ('C194', 'SCHOOL High (C194)'),
                          ('C195', 'SCHOOL Building Laboratory (C195)'),
                          ('C196', 'SCHOOL Building Computer Center (C196)'),
                          ('C197', 'COMMUNITY Post Office Branch (C197)'),
                          ('C198', 'WAREHOUSE Mega (C198)'),
                          ('C199', 'CARE Dental Clinic (C199)'),
                          ('C200', 'BANK Bank Main (C200)'),
                          ('C201', 'BANK Bank Mini (C201)'),
                          ('C202', 'TRANSPORT Passenger Terminal (C202)'),
                          ('C203', 'RESTAURANT Tavern (C203)'),
                          ('C204', 'WAREHOUSE Mini Storage Multi Story (C204)'),
                          ('C225', 'OTHER Condominium Non-Residential (C225)'),
                          ('C226', 'OTHER Special Use (C226)'),
                          ('C227', 'HOUSING Residence (C227)'),
                          ('C301', 'OFFICE Building Condominium (C301)'),
                          ('C302', 'WAREHOUSE Condominium (C302)'),
                          ('C303', 'STORE Retail Condominium (C303)'),
                          ('C304', 'BOAT Marina Condominium Slip (C304)'),
                          ('C305', 'OTHER Building Per Square Foot (C305)'),
                          ('C306', 'OTHER Building Per Unit (C306)'),
                          ('C307', 'HOUSING Residential Apartment Unit(s) (C307)'),
                          ('C308', 'HOUSING Rental Townhouse Unit(s) (C308)'),
                          ('C309', 'HOUSING Efficiency/Efficiencies (C309)'),
                          ('C310', 'HOUSING 1 Bedroom (C310)'),
                          ('C311', 'HOUSING 2 Bedrooms (C311)'),
                          ('C312', 'HOUSING 3 Bedrooms (C312)'),
                          ('C313', 'HOUSING 4 Bedrooms (C313)'),
                          ('C314', 'AUTO Parking Space (C314)'),
                          )
TOWN_CODE_DIGIT_TO_CHAR_VALUES = (("1001", "ALLE Cumberland"),
                                  ("1011", "ALLE Frostburg"),
                                  ("1201", "ALLE Barton"),
                                  ("1202", "ALLE Lonaconing"),
                                  ("1203", "ALLE Luke"),
                                  ("1204", "ALLE Midland"),
                                  ("1205", "ALLE Westernport"),
                                  ("2001", "ANNE Annapolis"),
                                  ("2002", "ANNE Highland Beach"),
                                  ("5001", "CALV Chesapeake Beach"),
                                  ("5002", "CALV North Beach"),
                                  ("6010", "CARO Denton"),
                                  ("6020", "CARO Federalsburg"),
                                  ("6030", "CARO Greensboro"),
                                  ("6040", "CARO Hillsboro"),
                                  ("6050", "CARO Marydel"),
                                  ("6060", "CARO Preston"),
                                  ("6070", "CARO Ridgely"),
                                  ("6080", "CARO Goldsboro"),
                                  ("6090", "CARO Henderson"),
                                  ("6100", "CARO Templeville"),
                                  ("7011", "CARR Taneytown"),
                                  ("7051", "CARR Sykesville"),
                                  ("7061", "CARR Manchester"),
                                  ("7071", "CARR Westminster"),
                                  ("7081", "CARR Hampstead"),
                                  ("7111", "CARR New Windsor"),
                                  ("7121", "CARR Union Bridge"),
                                  ("7131", "CARR Mount Airy"),
                                  ("8010", "CECI Cecilton"),
                                  ("8020", "CECI Chesapeake City"),
                                  ("8030", "CECI Elkton"),
                                  ("8040", "CECI North East"),
                                  ("8050", "CECI Charlestown"),
                                  ("8060", "CECI Rising Sun"),
                                  ("8070", "CECI Port Deposit"),
                                  ("8080", "CECI Perryville"),
                                  ("9010", "CHAR Indian Head"),
                                  ("9029", "CHAR La Plata"),
                                  ("9030", "CHAR Port Tobacco"),
                                  ("10001", "DORC Secretary"),
                                  ("10002", "DORC East New Market"),
                                  ("10003", "DORC Cambridge"),
                                  ("10004", "DORC Hurlock"),
                                  ("10005", "DORC Vienna"),
                                  ("10006", "DORC Church Creek"),
                                  ("10007", "DORC Galestown"),
                                  ("10008", "DORC Brookview"),
                                  ("10009", "DORC Eldorado"),
                                  ("11001", "FRED Brunswick"),
                                  ("11002", "FRED Burkittsville"),
                                  ("11003", "FRED Emmitsburg"),
                                  ("11004", "FRED Frederick City"),
                                  ("11005", "FRED Middletown"),
                                  ("11006", "FRED Mount Airy"),
                                  ("11007", "FRED Myersville"),
                                  ("11008", "FRED New Market"),
                                  ("11009", "FRED Rosemont"),
                                  ("11010", "FRED Thurmont"),
                                  ("11011", "FRED Walkersville"),
                                  ("11012", "FRED Woodsboro"),
                                  ("12264", "GARR Accident"),
                                  ("12300", "GARR Deer Park"),
                                  ("12312", "GARR Friendsville"),
                                  ("12324", "GARR Grantsville"),
                                  ("12336", "GARR Kitzmiller"),
                                  ("12348", "GARR Loch Lynn"),
                                  ("12360", "GARR Mountain Lake Park"),
                                  ("12372", "GARR Oakland"),
                                  ("13200", "HARF Aberdeen"),
                                  ("13300", "HARF Bel Air"),
                                  ("13600", "HARF Havre De Grace"),
                                  ("15010", "KENT Betterton"),
                                  ("15020", "KENT Chestertown"),
                                  ("15030", "KENT Galena"),
                                  ("15040", "KENT Millington"),
                                  ("15050", "KENT Rock Hall"),
                                  ("16001", "MONT Friendship Heights"),
                                  ("16002", "MONT Drummond"),
                                  ("16003", "MONT Oakmont"),
                                  ("16004", "MONT Chevy Chase Village"),
                                  ("16005", "MONT Chevy Chase Sec. 3"),
                                  ("16006", "MONT Chevy Chase Town of"),
                                  ("16007", "MONT Chevy Chase Sec. 5"),
                                  ("16008", "MONT Martins Addition"),
                                  ("16009", "MONT Chevy Chase North"),
                                  ("16010", "MONT Chevy Chase View"),
                                  ("16011", "MONT Battery Park"),
                                  ("16012", "MONT Rockville"),
                                  ("16013", "MONT Gaithersburg"),
                                  ("16014", "MONT Barnesville"),
                                  ("16015", "MONT Laytonsville"),
                                  ("16016", "MONT Poolesville"),
                                  ("16017", "MONT Garrett Park"),
                                  ("16018", "MONT Glen Echo"),
                                  ("16019", "MONT Somerset"),
                                  ("16020", "MONT Brookville"),
                                  ("16021", "MONT Washington Grove"),
                                  ("16022", "MONT Kensington"),
                                  ("16023", "MONT Takoma Park"),
                                  ("17072", "PRIN New Carrollton"),
                                  ("17073", "PRIN Eagle Harbor"),
                                  ("17074", "PRIN Greenbelt"),
                                  ("17075", "PRIN Berwyn Heights"),
                                  ("17076", "PRIN Bladensburg"),
                                  ("17077", "PRIN Bowie"),
                                  ("17078", "PRIN Brentwood"),
                                  ("17079", "PRIN Capitol Heights"),
                                  ("17080", "PRIN Cheverly"),
                                  ("17081", "PRIN College Park"),
                                  ("17082", "PRIN Colmar Manor"),
                                  ("17083", "PRIN Cottage City"),
                                  ("17084", "PRIN District Heights"),
                                  ("17085", "PRIN Edmonston"),
                                  ("17086", "PRIN Fairmount Heights"),
                                  ("17087", "PRIN Glenarden"),
                                  ("17088", "PRIN Hyattsville"),
                                  ("17089", "PRIN Landover Hills"),
                                  ("17090", "PRIN Laurel"),
                                  ("17091", "PRIN Mount Rainier"),
                                  ("17092", "PRIN North Brentwood"),
                                  ("17093", "PRIN Riverdale Park"),
                                  ("17094", "PRIN Seat Pleasant"),
                                  ("17096", "PRIN University Park"),
                                  ("17097", "PRIN Upper Marlboro"),
                                  ("17098", "PRIN Morningside"),
                                  ("17099", "PRIN Forest Heights"),
                                  ("18001", "QUEE Sudlersville"),
                                  ("18002", "QUEE Church Hill"),
                                  ("18003", "QUEE Centreville"),
                                  ("18004", "QUEE Queenstown"),
                                  ("18005", "QUEE Queen Anne"),
                                  ("18006", "QUEE Templeville"),
                                  ("18008", "QUEE Barclay"),
                                  ("18040", "QUEE Millington"),
                                  ("19100", "STMA Leonardtown"),
                                  ("20001", "SOME Crisfield"),
                                  ("20002", "SOME Princess Anne"),
                                  ("21001", "TALB Easton"),
                                  ("21002", "TALB St. Michaels"),
                                  ("21003", "TALB Trappe"),
                                  ("21004", "TALB Oxford"),
                                  ("21005", "TALB Queen Anne"),
                                  ("22010", "WASH Sharpsburg"),
                                  ("22020", "WASH Williamsport"),
                                  ("22030", "WASH Hagerstown"),
                                  ("22040", "WASH Clear Spring"),
                                  ("22050", "WASH Hancock"),
                                  ("22060", "WASH Boonesboro"),
                                  ("22070", "WASH Smithsburg"),
                                  ("22100", "WASH Funkstown"),
                                  ("22190", "WASH Keedysville"),
                                  ("23001", "WICO Salisbury"),
                                  ("23002", "WICO Mardela Springs"),
                                  ("23003", "WICO Pittsville"),
                                  ("23004", "WICO Sharptown"),
                                  ("23005", "WICO Delmar"),
                                  ("23006", "WICO Willards"),
                                  ("23007", "WICO Hebron"),
                                  ("23008", "WICO Fruitland"),
                                  ("24001", "WORC Pocomoke City"),
                                  ("24002", "WORC Snow Hill"),
                                  ("24003", "WORC Berlin"),
                                  ("24010", "WORC Ocean City"),
                                  ("24101", "WORC Ocean City"),
                                  ("24102", "WORC Ocean City"),
                                  ("24103", "WORC Ocean City"),
                                  ("24104", "WORC Ocean City"),
                                  ("24105", "WORC Ocean City"),
                                  ("24106", "WORC Ocean City"),
                                  ("24107", "WORC Ocean City"),
                                  ("24108", "WORC Ocean City"),
                                  ("24109", "WORC Ocean City"),
                                  )