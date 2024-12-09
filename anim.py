import arcade

from itertools import chain

class Animator:
    """
    Manages sprite sheets with many animations laid out in a
    grid format. 
    """
    def __init__(self, filepath, dimensions, cols, rows):
        """
        Loads image, sets up surface, and initializes state.

        @filepath : Path to image file.
        @dimensions : Tuple of (width, height) of a single frame's dimensions.
        @cols : Number of sprite frames on each row.
        @rows : Number of rows of sprite frames.
        """
        w, h = dimensions
        frame_locs = list(chain(
            [[(x, y, w, h) for x in range(0, w*cols, w)] for y in range(0, h*rows, h)]
        ))[0]
        self.frames = arcade.load_textures(filepath, frame_locs)
        self.frames_flip = arcade.load_textures(filepath, frame_locs, mirrored=True)

        self.anims = dict()
        self.anim_curr = None
        self.anim_i = 0
        self.active_frames = self.frames

    def registerAnim(self, name, *frames):
        """
        Add a new named animation with a list of frames that should
        be displayed in the animation routine.
        @name : String name of the animation.
        @frames : List of (x,y) pairs representing frames, where x is the
        column and y is the row. Starts at 0,0 in the upper left.
        """
        # note that *frames corresponds to the unpacking seen
        # in Player.__init__(). What this *frames represents
        # is a wildcard object, where every argument given after
        # `name` is packed into a list known as `frames`.
        self.anims[name] = frames

    def flipHoriz(self, flip):
        """
        Flips the entire spritesheet and marks itself as flipped
        or unflipped for frame rect calculations in `Animator.next()`.
        @flip : Marks whether the frames should be flipped or unflipped.
        `False` matches original orientation, `True` matches flipped
        orientation.
        """
        self.active_frames = self.frames_flip if flip else self.frames

    def change(self, name):
        """
        Switches the animation based on a name pre-registered 
        using `Animator.registerAnim()`.
        @name: Name of the animation to switch to.
        """
        self.anim_curr = name
        self.anim_i = 0

    def next(self):
        """
        Advances the animation forward a frame.
        Returns the next texture to render.
        """
        self.anim_i += 1
        anim_len = len(self.anims[self.anim_curr])
        if self.anim_i >= anim_len:
            self.anim_i = 0

    @property
    def texture(self):
        return self.active_frames[self.anims[self.anim_curr][self.anim_i]]
