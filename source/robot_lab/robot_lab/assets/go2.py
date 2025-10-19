# Copyright (c) 2025 Qiming-Hou

import isaaclab.sim as sim_utils
from isaaclab.actuators import DCMotorCfg, ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

from robot_lab.assets import ISAACLAB_ASSETS_DATA_DIR

##
# Configuration
##


UNITREE_GO2_ARM_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        fix_base=False,
        merge_fixed_joints=True,
        replace_cylinders_with_capsules=False,
        asset_path=f"{ISAACLAB_ASSETS_DATA_DIR}/Robots/go2_with_airbot/urdf/go2_with_airbot_vis_flip.urdf",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
         articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
        joint_drive=sim_utils.UrdfConverterCfg.JointDriveCfg(
            gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=0, damping=0)
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38),
        joint_pos={
            ".*L_hip_joint": 0.0,
            ".*R_hip_joint": -0.0,
            "F.*_thigh_joint": 0.8,
            "R.*_thigh_joint": 0.8,
            ".*_calf_joint": -1.5,
            "airbot_.*": 0.0,
            # "left_joint": 0.0,
            # "right_joint": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        # "hip": DCMotorCfg(
        #     joint_names_expr=[".*_hip_joint"],
        #     effort_limit=23.5,
        #     saturation_effort=23.5,
        #     velocity_limit=30.0,
        #     stiffness=15.0,
        #     damping=0.5,
        #     friction=0.0,
        # ),
        # "thigh": DCMotorCfg(
        #     joint_names_expr=[".*_thigh_joint"],
        #     effort_limit=23.5,
        #     saturation_effort=23.5,
        #     velocity_limit=30.0,
        #     stiffness=15.0,
        #     damping=0.5,
        #     friction=0.0,
        # ),
        # "calf": DCMotorCfg(
        #     joint_names_expr=[".*_calf_joint"],
        #     effort_limit=23.5,
        #     saturation_effort=23.5,
        #     velocity_limit=30.0,
        #     stiffness=15.0,
        #     damping=0.5,
        #     friction=0.0,
        # ),
        # "arm": DCMotorCfg(
        #     joint_names_expr=["airbot_.*"],
        #     effort_limit=23.5,
            
        #     saturation_effort=23.5,
        #     velocity_limit=30.0,
        #     stiffness=10.0,
        #     damping=0.5,
        #     friction=0.0,
        # ),
                # Legs: all 12 leg joints, tightly scoped so they never match arm joints
        "legs": DCMotorCfg(
            joint_names_expr=[r"^(FL|FR|RL|RR)_(hip|thigh|calf)_joint$"],
            effort_limit=23.5,
            saturation_effort=23.5,
            velocity_limit=30.0,
            stiffness=25.0,
            damping=0.5,
            friction=0.0,
        ),
        # Arm: 6 revolute joints (airbot_j1..airbot_j6)
        "arm": DCMotorCfg(
            joint_names_expr=[r"^airbot_j[1-6]$"],
            effort_limit=30.0,
            saturation_effort=30.0,
            velocity_limit=10.0,
            stiffness=20.0,
            damping=0.5,
            friction=0.0,
        ),
    },
)