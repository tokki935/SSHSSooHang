import abc


class Env:

    def __init__(
        self,
        world_map: dict["Entity", tuple[int, int]] = {},
        tiles: list[list["Tile"]] = [],
    ):

        self.world_map = world_map

        self.tiles = tiles

    def update(self):

        for e in self.world_map.keys():

            for b in e.behaviors():

                if b.determine(e, self):

                    b.act(e, self)

                    break


class Tile: ...


class Entity(abc.ABC):

    @abc.abstractmethod
    def behaviors(self) -> list["Behavior"]: ...


class Hyena(Entity):

    def behaviors(self):

        return [
            StealFoodFrom([Cheetah, Lion]),
            Hunt([Zebra, Rabbit]),
        ]


class Behavior(abc.ABC):

    @abc.abstractmethod
    def determine(self, entity: "Entity", env: "Env") -> bool: ...

    @abc.abstractmethod
    def act(self, entity: "Entity", env: "Env") -> None: ...


class Hunt(Behavior):

    def __init__(self, target_classes):

        self.target_classes = target_classes

    def __check_target(self, target):

        return any(
            isinstance(target, target_class) for target_class in self.target_classes
        )

    def determine(self, entity, env):

        return self.entity.is_hungry()

    def act(self, entity, env):

        for e in env.find_within(entity, self.인지범위):

            if self.__check_target(e):

                e방향으로_위치변경()
