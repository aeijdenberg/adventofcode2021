import itertools

class Scanner(object):
    def __init__(self, id, b=None):
        self.id = id
        self.beacons = b if b else set()
    def __repr__(self):
        return repr(self.beacons)
    def each_combo(self):
        for pos_neg in itertools.product(*([[1,-1]]*3)):
            for orders in itertools.permutations(range(3)):
                yield Scanner(self.id, set(
                    tuple(pos_neg[i] * xyz[orders[i]] for i in range(3)) for xyz in self.beacons
                ))

    def overlaps(self, other, target):
        for our_xyz in self.beacons:
            for their_xyz in other.beacons:
                offsets = list(their_xyz[i] - our_xyz[i] for i in range(3))
                offset_scanner = Scanner(other.id, set(
                    tuple(b[i] - offsets[i] for i in range(3)) for b in other.beacons
                ))
                if len(self.beacons & offset_scanner.beacons) >= target:
                    print("GOT ONE!!!")
                    return offset_scanner
        return None


scanners = []
for line in open('input'):
    if line.startswith('---'):
        scanners.append(Scanner(len(scanners)))
    elif line.strip():
        scanners[-1].beacons.add(tuple([int(x) for x in line.strip().split(',')]))

known_bads = set()

done_scanners, scanners = [scanners[0]], scanners[1:]
while len(scanners):
    done = False
    for idx, scanner in enumerate(scanners):
        for good_scanner in done_scanners:
            key = tuple(sorted([good_scanner.id, scanner.id]))
            if key in known_bads:
                continue
            print(key)
            for version in scanner.each_combo():
                adjusted_scanner = good_scanner.overlaps(version, 12)
                if adjusted_scanner is not None:
                    done_scanners = [adjusted_scanner] + done_scanners
                    scanners = scanners[:idx] + scanners[idx+1:]
                    done = True
                    break
            if done:
                break
            else:
                known_bads.add(key)
        if done:
            break
    if not done:
        print("Giving up, no change.")
        break

unique_points = set()
for scanner in done_scanners:
    unique_points |= scanner.beacons
print(unique_points)
print(len(unique_points))