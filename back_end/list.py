unilist = [['princeton'],['harvard'],[' mit ','massachusetts institute of technology'],['yale'],['stanford'],['uchicago','university of chicago'],['upenn','university of pennsylvania'],['caltech','california institute of technology'],['duke'],['jhu','john hopkin'],['northwestern',' nu '],['dartmouth'],['brown'],['vanderbilt'],['washu','washington university'],['cornell'],['rice'],['university of notre dame',' und ','notre dame'],['ucla','uc los angeles','university of califonia los angeles'],['emory'],['uc berkeley','berkeley',' ucb '],['georgetown'],['umich','university of michigan'],['cmu','carnegie mellon'],[' uva ','university of virginia'],[' usc ','university of southern california'],['nyu','new york university'],['tufts'],['ucsb','santa barbara'],[' uf ','university of florida'],['unc','university of north carolina at chapel hill'],['wake forest'],['ucsd','san diego'],['university of rochester','rochester'],['boston college'],['uci','irvine'],['gatech','gtech','georgia tech'],['uc davis','davis','ucd'],['ut austin',' uta ','austin'],['william & mary','william and mary'],[' bu ','boston university','bostonu'],['brandeis'],['cwru','case western'],['tulane'],['uw madison', 'madison'],['uiuc','university of illinois','urbana','gies'],['uga','university of georgia'],['lehigh'],['northeastern','neu'],['osu','ohio state'],['pepperdine'],['purdue'],['villanova'],['williams'],['amherst college'],['swarthmore'],['pomona'],['wellesley'],['bowdoin'],['claremont','cmc'],['carleton'],['middlebury'],['washington & lee','washington and lee'],['davidson'],['grinnell'],['hamilton'],['haverford'],['barnard'],['colby'],['colgate'],['smith'],['wesleyan']]
ecslist = {'internship','intern','interned','working','captain','apprenticeship','research','executive', 'officer','founder','co-founder','president','vice-president','vp','treasurer','secretary','club','job','nonprofit','volunteering','volunteer','volunteered','tutor','tutoring','teaching','art','football','soccer','tennis','golf','mun','robotics','yearbook','olympiad','orchestra'}
genderlist = [['male',' m','boy'],['female',' f','girl']]
racelist = ['white','hispanic','asian','black']
majorlist = [['math','stats','statistics'],['physics'],['bio'],['premed','med'],['neuroscience','cognitive','behavioral'],['chemistry','chem'],['computer science',' cs'],['mechanical engineer','mech e','meche'],['chemical engineer','cheme','chem e'],['computer engineering','ce '],['electrical engineering','ee ',],['aerospace engineering','aero'],['econ'],['finance'],['business','biz','management'],['marketing'],['history'],['political science','poli sci','political'],['philosophy','phil'],['law'],['english'],['undecided'],['arts'],['anthropology','anthro'],['environmental','enviro','earth'],[' international relations',' ir '],['nursing'],['sociology'],['psychology']]
unilist2 = []
for i in range(len(majorlist)):
    unilist2.append(majorlist[i][0].capitalize())
print(unilist2)

