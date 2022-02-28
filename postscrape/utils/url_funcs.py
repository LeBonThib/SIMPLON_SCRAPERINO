def get_recherche_oeuvre_url():
    urls = []
    with open('.\\url.txt') as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace('"','')
            if "recherche/oeuvre" in line:
                urls.append(line)
        return urls