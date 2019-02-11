import itertools as it
import numpy as np
import matplotlib.pyplot as plt

# Format: (x, y, radius)
circles = [(0.6, -0.6, 0.2),
           (-0.4, 0.3, 0.4)]

# Format: (x_min, y_min, x_max, y_max)
rectangles = [(-0.3, -0.1, -0.7, -0.5),
              (0.8, 0.9, 0.3, 0.6)]

# Format: (x, y, angle_min, angle_max)
cameras = [(-0.95, -0.95, -0.5, np.pi / 2 + 0.5),
           (-0.95, 0.95, -np.pi / 2 - 0.5, 0.5),
           (0.95, 0.95, np.pi - 0.5, (3/2) * np.pi + 0.5),
           (0.95, -0.95, np.pi / 2 - 0.5, np.pi + 0.5),
           (0.3, 0, 0, 2 * np.pi),
           (-0.9, 0, 0, 2 * np.pi),
           (-0.3, 0.9, 0, 2 * np.pi),
           (0, -0.9, 0, 2 * np.pi),
           (0.97, 0.3, 0, 2 * np.pi)]


# Ground truth functions
def is_inside_wall(point):
    '''
    Decides whether a point is inside a wall of the room.
    '''
    x, y = point
    return (x < -1) or (x > 1) or (y < -1) or (y > 1)


def is_inside_shape(point):
    '''
    Decides whether a point is inside any shape in the room.
    '''
    x, y = point

    # Circles
    for center_x, center_y, radius in circles:
        dist_squared = (center_x - x) ** 2 + (center_y - y) ** 2
        if dist_squared < radius ** 2:
            return True

    # Rectangles
    for x_min, x_max, y_min, y_max in rectangles:
        if x_min < x < x_max and y_min < y < y_max:
            return True

    # Not inside any shape
    return False


def is_inside_object(point):
    '''
    Decides whether a point is inside any object (wall or shape).
    '''
    return is_inside_wall(point) or is_inside_shape(point)


# Data generating functions
def raytrace_ray(cam_x, cam_y, angle, step=0.05):
    '''
    Returns a positive point and a list of negative points along a ray.

    cam_x, cam_y: the ray's origin
    angle: angle of ray from camera, in radians
    step: distance to move along the ray at each step

    Returns: (pos, negs)
        pos: (x, y) of the contact point
        neg: [(x, y)] of non-contact points
    '''
    negs = []
    x, y = cam_x, cam_y
    while not is_inside_object((x, y)):
        negs.append((x, y))
        x += step * np.cos(angle)
        y += step * np.sin(angle)
    return ((x, y), negs)


def raytrace_cam(cam_x, cam_y, min_angle, max_angle,
                 step_r=0.05, step_angle=0.05):
    '''
    Returns positive and negative points along rays sampled from a camera.

    cam_x, cam_y: the ray's origin
    min_angle, max_angle: range of angles to sample
    step_r: distance to move along the ray at each radial step
    step_angle: radians to advance ray at each angular step

    Returns: (pos, negs)
        pos: [(x, y)] of contact points
        neg: [(x, y)] of non-contact points
    '''
    angles = np.arange(min_angle, max_angle, step_angle)
    rays = [raytrace_ray(cam_x, cam_y, angle, step_r) for angle in angles]
    pos, neg = zip(*rays)
    neg = list(it.chain.from_iterable(neg))
    return (pos, neg)


def raytrace_cams(cams, step_r=0.02, step_angle=0.05):
    '''
    raytrace_cam for multiple cameras
    '''
    raytraces = [raytrace_cam(cam[0], cam[1], cam[2], cam[3],
                              step_r, step_angle) for cam in cams]
    pos, neg = zip(*raytraces)
    pos = list(it.chain.from_iterable(pos))
    neg = list(it.chain.from_iterable(neg))
    return (pos, neg)


# Plotting functions
def plot_scene_true(n_points=150, axes=None):
    if not axes:
        _, axes = plt.subplots()

    pts = np.linspace(-1.1, 1.1, n_points)
    inside_pts = [(x, y) for y in pts for x in pts if is_inside_object((x, y))]

    inside_xs, inside_ys = zip(*inside_pts)
    axes.scatter(inside_xs, inside_ys)


def plot_scene_raytaced(pos, neg, axes=None):
    if not axes:
        _, axes = plt.subplots()

    pos_x, pos_y = zip(*pos)
    neg_x, neg_y = zip(*neg)

    axes.scatter(neg_x, neg_y, c='red')
    axes.scatter(pos_x, pos_y, c='green', s=100)


# Main program: plot sscene, and generate data files
if __name__ == '__main__':
    _, axes = plt.subplots()
    pos, neg = raytrace_cams(cameras)

    print('Raytraced %d positive points and %d negative points' %
          (len(pos), len(neg)))

    # Save data
    np.savetxt('./data/positives.txt', pos)
    np.savetxt('./data/negatives.txt', neg)

    # Plot data
    plot_scene_true(axes=axes)
    plot_scene_raytaced(pos, neg, axes)
    plt.title('Full scene')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(['True objects', 'Negative data', 'Positive data'])
    plt.show()
