


def report():
  genres = {}

  f = open("before.txt")
  beforeval = [i.strip() for i in f.readlines()]
  f.close()

  labels = []

  s = ""

  valueses = {}

  values = []


  f = open("report.txt")
  lines = f.readlines()
  for line in lines:
    label = line.split(":")[0].strip()[:-5]
    value = int(line.split(":")[1].strip())

    labels.append(label)

    if(label in genres):
      genres[label] += 1

    else:
      genres[label] = 1

    valueses[value] = label


    values.append(value)


  f.close()

  for i in genres:
    s += "There "+ ("are " if genres[i] > 1 else "is ") + str(genres[i]) + " " + i +("s " if genres[i] > 1 else " ") + (" and " if len(genres) > 1 else "")


  vv = sorted(values,reverse = True)
  first = ""
  behind = ""
  if(len(vv) > 0):
    for i in range(len(vv)):
      first = vv[0]
      behind = vv[i]
      if behind == first:
        continue
      else:
        break

    s += ("There is a " + valueses[behind] + " behind the " + valueses[first] + ".") if len(genres) > 1 else "."


  if(sorted(labels) != sorted(beforeval)):
    f = open("before.txt","w")
    for i in labels:
      f.write(i + "\n")
    f.close()
    return s




