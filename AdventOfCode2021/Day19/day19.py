#THIS SPAGHETTI REALLY COULD USE SOME LOVE --- Runtime 7 min ---
from itertools import product

import numpy as np


def getRotationMatrix():
  rotations = list(product(*[[0, 90, 180, 270], [0, 90, 180, 270], [0, 90, 180, 270]]))
  s = set()
  rot_matrices = []
  for rot in rotations:
    alpha_rad = np.deg2rad(rot[0])
    beta_rad = np.deg2rad(rot[1])
    gamma_rad = np.deg2rad(rot[2])
    rot_mat = np.array([
      [round(np.cos(alpha_rad) * np.cos(beta_rad)),
       round(np.cos(alpha_rad) * np.sin(beta_rad) * np.sin(gamma_rad) - np.sin(alpha_rad) * np.cos(gamma_rad)),
       round(np.cos(alpha_rad) * np.sin(beta_rad) * np.cos(gamma_rad) + np.sin(alpha_rad) * np.sin(gamma_rad))],
      [round(np.sin(alpha_rad) * np.cos(beta_rad)),
       round(np.sin(alpha_rad) * np.sin(beta_rad) * np.sin(gamma_rad) + np.cos(alpha_rad) * np.cos(gamma_rad)),
       round(np.sin(alpha_rad) * np.sin(beta_rad) * np.cos(gamma_rad) - np.cos(alpha_rad) * np.sin(gamma_rad))],
      [round(-np.sin(beta_rad)), round(np.cos(beta_rad) * np.sin(gamma_rad)),
       round(np.cos(beta_rad) * np.cos(gamma_rad))]
    ])
    if tuple(rot_mat.flatten()) not in s:
      rot_matrices.append((rot, rot_mat))
    s.add(tuple(rot_mat.flatten()))
  return rot_matrices




class Scanner:
    scanner_rel_s0 = None
    beacons_rel_s0 = None
    right_rot_mat = None
    matching_scanner = None

    def __init__(self, data):
        self.scannerID = int(data.split("\n")[0].split("scanner ")[1].split(" ---")[0])
        self.beacons = np.array(
            [(int(x.split(",")[0]), int(x.split(",")[1]), int(x.split(",")[2])) for x in data.split("\n")[1:]])



def checkIfBeaconsInCommon(s_with_0, s2):
    rotations = getRotationMatrix()
    for rot, rot_mat in rotations:
        shared_beacon = 0
        sw0_beacons = np.matmul(s_with_0.beacons, s_with_0.right_rot_mat)
        s2_beacons = np.matmul(s2.beacons, rot_mat)
        for sw0_beacon in sw0_beacons:
            sw0_ref_beacons = sw0_beacons - sw0_beacon
            for s2_beacon in s2_beacons:
                s2_ref_beacons = s2_beacons - s2_beacon
                for s2_ref_beacon in s2_ref_beacons:
                    if s2_ref_beacon.tolist() != [0, 0, 0] and s2_ref_beacon.tolist() in sw0_ref_beacons.tolist():
                        tmp_coord = np.array(s_with_0.scanner_rel_s0 + sw0_beacon + s2_ref_beacon)
                        shared_beacon += 1
                        proposed_s2_coord_rel_0 = np.array(tmp_coord - (s2_ref_beacon + s2_beacon))

            if shared_beacon >= 12:
                s2.right_rot_mat = rot_mat
                s2.scanner_rel_s0 = proposed_s2_coord_rel_0
                s2.beacons_rel_s0 = proposed_s2_coord_rel_0 + s2_beacons
                s2.matching_scanner = s_with_0.scannerID
                return True
    return False


def main():
    data = open("input.txt").read().split("\n\n")
    scanners = [Scanner(x) for x in data]
    scanners[0].scanner_rel_s0 = np.array([0, 0, 0])
    scanners[0].beacons_rel_s0 = scanners[0].beacons
    scanners[0].right_rot_mat = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    scanners_done = [scanners.pop(0)]
    s_list = []
    is_done = False

    while scanners:
        s = scanners.pop(0)
        if len(scanners_done) <= len(s_list) and s.scannerID != s_list[len(scanners_done) - 1][0]:
            scanners.append(s)
            continue
        elif len(scanners_done) <= len(s_list) and s.scannerID == s_list[len(scanners_done) - 1][0]:
            for s_done in scanners_done:
                if s_done.scannerID == s_list[len(scanners_done) - 1][1]:
                    is_done = checkIfBeaconsInCommon(s_done, s)
                    print("Done with scanner: " + str(s.scannerID) + " matching with scanner: " + str(s_done.scannerID))
                    print(str(len(scanners)) + " scanners to go.")
                    scanners_done.append(s)
                    break
            continue

        for s_done in scanners_done:
            is_done = checkIfBeaconsInCommon(s_done, s)
            if is_done:
                break
        if is_done:
            print("Done with scanner: " + str(s.scannerID) + " matching with scanner: " + str(s_done.scannerID))
            print(str(len(scanners)) + " scanners to go.")
            scanners_done.append(s)
        else:
            scanners.append(s)

    seen_beacons = set()
    for s in scanners_done:
        for beacon in s.beacons_rel_s0:
            seen_beacons.add((round(beacon[0]), round(beacon[1]), round(beacon[2])))
    seen = list(seen_beacons)
    seen.sort()
    print(seen)
    print(f"Solution 1: {len(seen)}")

    max_dist = 0
    for s1 in scanners_done:
        for s2 in scanners_done:
            manh_dist = abs(s1.scanner_rel_s0[0] - s2.scanner_rel_s0[0]) + abs(s1.scanner_rel_s0[1] - s2.scanner_rel_s0[1]) + abs(s1.scanner_rel_s0[2] - s2.scanner_rel_s0[2])
            if manh_dist > max_dist:
                max_dist = manh_dist
    print(f"Solution 2: {max_dist}")


if __name__ == "__main__":
    main()
