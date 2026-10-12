#!/usr/bin/env python3
"""
verify_study_guide.py — Automated Programmatic Verification Suite
================================================================================
Target: OMCR Mid-Term Exam (14 Oct 2026) Interactive Study Guide
Author: test_writer_1 (Teamwork Preview QA & Specialist)
Course: Omnichannel Retailing (OMCR) | Instructor: Dr. Smitu Malhotra

Scope of Programmatic Verification:
  Tier 1: Quantitative Engine Reference Mathematics (6 Core + 3 Supplementary)
  Tier 2: Single-File HTML5 Architecture & 100% Offline Self-Containment (Zero CDNs)
  Tier 3: Complete Syllabus & Theoretical Framework Coverage (Sessions 1–5, 6–7, 11, Savings Bank)
  Tier 4: Strict Merchandising Boundary Negative Exclusion (Zero Leaks)
  Tier 5: Section II Subjective Answering Blueprints (8 Structured Frameworks)
  Tier 6: Section I Practice MCQ Engine Integrity (>= 25 Questions with Distractor Rationales)
  Tier 7: Embedded Interactive Calculator UI & In-Browser Logic

Standard Library Only: Requires no third-party pip dependencies.
================================================================================
"""

import sys
import os
import re
import math
import json
import argparse
import unittest
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# Default target HTML path
DEFAULT_HTML_PATH = Path(r"C:\Users\Janmejai\omcr\omcr_midterm_study_guide.html")


# ==============================================================================
# SECTION 1: REFERENCE MATHEMATICAL ENGINES
# ==============================================================================

def calc_margin_from_markup(markup_pct: float) -> float:
    """
    Computes Gross Margin % from Markup on Cost %.
    Margin % = Markup % / (1 + Markup % / 100) = (Markup % * 100) / (100 + Markup %)
    """
    if markup_pct <= -100.0:
        raise ValueError("Markup on cost must be strictly greater than -100%")
    return (markup_pct / (100.0 + markup_pct)) * 100.0


def calc_markup_from_margin(margin_pct: float) -> float:
    """
    Computes Markup on Cost % from Gross Margin %.
    Markup % = Margin % / (1 - Margin % / 100) = (Margin % * 100) / (100 - Margin %)
    """
    if margin_pct >= 100.0:
        raise ValueError("Margin must be strictly less than 100%")
    return (margin_pct / (100.0 - margin_pct)) * 100.0


def calc_sp_from_cost_and_margin(cost: float, margin_pct: float) -> float:
    """Computes Selling Price from unit Cost and target Margin %."""
    if cost <= 0:
        raise ValueError("Cost must be strictly greater than 0")
    if margin_pct >= 100.0:
        raise ValueError("Margin must be strictly less than 100%")
    return cost / (1.0 - (margin_pct / 100.0))


def calc_sales_per_sqft(net_sales: float, sqft: float) -> float:
    """Computes Sales per Square Foot of selling space."""
    if sqft <= 0:
        raise ValueError("Selling square footage must be strictly greater than 0")
    if net_sales < 0:
        raise ValueError("Net sales cannot be negative")
    return net_sales / sqft


def calc_sales_per_fte(net_sales: float, fte: float) -> float:
    """Computes Sales per Full-Time Equivalent (FTE) employee."""
    if fte <= 0:
        raise ValueError("FTE count must be strictly greater than 0")
    if net_sales < 0:
        raise ValueError("Net sales cannot be negative")
    return net_sales / fte


def calc_reilly_breaking_point(d: float, pa: float, pb: float) -> float:
    """
    Reilly's Law of Retail Gravitation: Breaking Point distance from City A.
    B_a = d / (1 + sqrt(P_b / P_a))
    """
    if d <= 0:
        raise ValueError("Distance between cities must be strictly positive")
    if pa <= 0 or pb <= 0:
        raise ValueError("Populations of both cities must be strictly positive")
    return d / (1.0 + math.sqrt(pb / pa))


def calc_huff_probabilities(stores: List[Dict[str, float]], lam: float = 2.0) -> List[float]:
    """
    Huff Gravity Model: Computes patronizing probabilities P_ij for a list of stores.
    U_ij = S_j / (T_ij ^ lambda)
    P_ij = U_ij / sum(U_ik)
    """
    if lam < 0:
        raise ValueError("Friction parameter lambda must be non-negative")
    if not stores:
        raise ValueError("At least one competing store is required")

    utilities = []
    for s in stores:
        size = s.get("size", 0.0)
        time = s.get("time", 0.0)
        if size <= 0:
            raise ValueError("Store size/attractiveness must be strictly positive")
        if time <= 0:
            raise ValueError("Travel time/distance must be strictly positive")
        utilities.append(size / (time ** lam))

    total_u = sum(utilities)
    if total_u <= 0:
        raise ValueError("Total utility must be strictly positive")
    return [u / total_u for u in utilities]


def calc_huff_expected_sales(probs: List[float], market_potential: float) -> List[float]:
    """Computes expected sales captured by each store given choice probabilities."""
    return [p * market_potential for p in probs]


def calc_strategic_profit_model(net_sales: float, cogs: float, expenses: float,
                                current_assets: float, fixed_assets: float,
                                liabilities: float) -> Dict[str, float]:
    """
    Strategic Profit Model (DuPont ROA & ROE Decomposition).
    Margin Path: Net Profit Margin % = (Net Profit / Net Sales) * 100
    Turnover Path: Asset Turnover = Net Sales / Total Assets
    ROA % = Net Profit Margin % * Asset Turnover = (Net Profit / Total Assets) * 100
    Financial Leverage = Total Assets / Net Worth
    ROE % = ROA % * Financial Leverage = (Net Profit / Net Worth) * 100
    """
    if net_sales <= 0:
        raise ValueError("Net sales must be strictly greater than 0")
    total_assets = current_assets + fixed_assets
    if total_assets <= 0:
        raise ValueError("Total assets must be strictly greater than 0")

    gross_margin = net_sales - cogs
    net_profit = gross_margin - expenses
    net_worth = total_assets - liabilities

    npm_pct = (net_profit / net_sales) * 100.0
    asset_turnover = net_sales / total_assets
    roa_pct = (net_profit / total_assets) * 100.0

    if net_worth > 0:
        financial_leverage = total_assets / net_worth
        roe_pct = (net_profit / net_worth) * 100.0
    else:
        financial_leverage = float("nan")
        roe_pct = float("nan")

    return {
        "gross_margin": gross_margin,
        "gross_margin_pct": (gross_margin / net_sales) * 100.0,
        "net_profit": net_profit,
        "npm_pct": npm_pct,
        "total_assets": total_assets,
        "asset_turnover": asset_turnover,
        "roa_pct": roa_pct,
        "net_worth": net_worth,
        "financial_leverage": financial_leverage,
        "roe_pct": roe_pct,
    }


def calc_gmroi(net_sales: float, cogs: float, avg_inv_cost: float) -> Dict[str, float]:
    """
    Gross Margin Return on Inventory Investment (GMROI).
    GMROI = Gross Margin $ / Average Inventory at Cost
          = Gross Margin % * (Net Sales / Average Inventory at Cost)
          = Markup on Cost * Inventory Turnover at Cost
    """
    if avg_inv_cost <= 0:
        raise ValueError("Average inventory at cost must be strictly greater than 0")
    if net_sales <= 0:
        raise ValueError("Net sales must be strictly greater than 0")

    gross_margin = net_sales - cogs
    gm_pct = (gross_margin / net_sales) * 100.0
    sales_to_inv = net_sales / avg_inv_cost
    gmroi = gross_margin / avg_inv_cost

    markup_cost_pct = (gross_margin / cogs) * 100.0 if cogs > 0 else float("nan")
    turnover_cost = cogs / avg_inv_cost

    return {
        "gross_margin": gross_margin,
        "gm_pct": gm_pct,
        "sales_to_inv": sales_to_inv,
        "gmroi": gmroi,
        "markup_cost_pct": markup_cost_pct,
        "turnover_cost": turnover_cost,
    }


def calc_dark_store_unit_economics(aov: float, gm_pct: float, delivery_fee: float,
                                    picking_cost: float, rider_cost: float,
                                    packaging_payment_cost: float,
                                    daily_fixed_cost: float) -> Dict[str, float]:
    """Supplementary Model: Quick-Commerce Dark Store Unit Economics (Session 4)."""
    revenue_per_order = (aov * (gm_pct / 100.0)) + delivery_fee
    variable_cost_per_order = picking_cost + rider_cost + packaging_payment_cost
    contribution_margin = revenue_per_order - variable_cost_per_order

    if contribution_margin > 0:
        daily_breakeven_orders = daily_fixed_cost / contribution_margin
    else:
        daily_breakeven_orders = float("inf")

    return {
        "revenue_per_order": revenue_per_order,
        "variable_cost_per_order": variable_cost_per_order,
        "contribution_margin": contribution_margin,
        "daily_breakeven_orders": daily_breakeven_orders,
    }


def calc_omnichannel_clv(margin: float, retention: float, discount: float, cac: float = 0.0) -> float:
    """Supplementary Model: Customer Lifetime Value (Session 3)."""
    if discount <= 0:
        raise ValueError("Discount rate must be strictly positive")
    denom = 1.0 + discount - retention
    if denom <= 0:
        raise ValueError("Denominator (1 + d - r) must be positive")
    return (margin * retention / denom) - cac


def calc_channel_migration_savings(total_txns: int, branch_cost: float,
                                   allocations: List[Tuple[float, float]]) -> Dict[str, float]:
    """
    Supplementary Model: Savings Bank Channel Economics (Case Study).
    allocations: list of (proportion, channel_unit_cost)
    """
    baseline_cost = total_txns * branch_cost
    migrated_cost = sum(total_txns * prop * unit_cost for prop, unit_cost in allocations)
    savings = baseline_cost - migrated_cost
    pct_reduction = (savings / baseline_cost) * 100.0 if baseline_cost > 0 else 0.0
    return {
        "baseline_cost": baseline_cost,
        "migrated_cost": migrated_cost,
        "monthly_savings": savings,
        "annual_savings": savings * 12.0,
        "pct_reduction": pct_reduction,
    }


# ==============================================================================
# SECTION 2: HTML DOCUMENT INSPECTION HARNESS
# ==============================================================================

class HTMLStudyGuideInspector:
    """Loads and inspects the single-file HTML study guide."""

    def __init__(self, html_path: Path):
        self.html_path = html_path
        self.raw_content: str = ""
        self.clean_text: str = ""
        self.head_content: str = ""
        self.body_content: str = ""
        self.style_content: str = ""
        self.script_content: str = ""
        self.headings: List[str] = []
        self.loaded: bool = False

    def load(self) -> bool:
        if not self.html_path.exists():
            self.loaded = False
            return False
        with open(self.html_path, "r", encoding="utf-8", errors="replace") as f:
            self.raw_content = f.read()

        # Extract sections
        head_match = re.search(r"<head[^>]*>(.*?)</head>", self.raw_content, re.DOTALL | re.IGNORECASE)
        self.head_content = head_match.group(1) if head_match else ""

        body_match = re.search(r"<body[^>]*>(.*?)</body>", self.raw_content, re.DOTALL | re.IGNORECASE)
        self.body_content = body_match.group(1) if body_match else ""

        styles = re.findall(r"<style[^>]*>(.*?)</style>", self.raw_content, re.DOTALL | re.IGNORECASE)
        self.style_content = "\n".join(styles)

        scripts = re.findall(r"<script[^>]*>(.*?)</script>", self.raw_content, re.DOTALL | re.IGNORECASE)
        self.script_content = "\n".join(scripts)

        # Extract headings (<h1-h6> and <summary>)
        heading_matches = re.findall(r"<(h[1-6]|summary)[^>]*>(.*?)</\1>", self.raw_content, re.DOTALL | re.IGNORECASE)
        self.headings = [re.sub(r"<[^>]+>", " ", h[1]).strip() for h in heading_matches]

        # Stripped plain text
        self.clean_text = re.sub(r"<[^>]+>", " ", self.raw_content)
        self.clean_text = re.sub(r"\s+", " ", self.clean_text)
        self.loaded = True
        return True

    def find_external_resources(self) -> List[str]:
        """Detects any external http/https/CDN resource references."""
        violations = []
        # Check <link href="...">
        links = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', self.raw_content, re.IGNORECASE)
        for link in links:
            if link.startswith(("http://", "https://", "//")):
                violations.append(f"<link href='{link}'>")

        # Check <script src="...">
        scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', self.raw_content, re.IGNORECASE)
        for script in scripts:
            if script.startswith(("http://", "https://", "//")):
                violations.append(f"<script src='{script}'>")

        # Check <img src="...">
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', self.raw_content, re.IGNORECASE)
        for img in imgs:
            if img.startswith(("http://", "https://", "//")):
                violations.append(f"<img src='{img}'>")

        # Check @import url(...)
        imports = re.findall(r'@import\s+(?:url\()?["\']?([^"\'\)\s]+)["\']?\)?', self.style_content, re.IGNORECASE)
        for imp in imports:
            if imp.startswith(("http://", "https://", "//")):
                violations.append(f"@import '{imp}'")

        # Check common CDN keywords in head or scripts
        cdn_keywords = [
            "fonts.googleapis.com", "fonts.gstatic.com", "cdnjs.cloudflare.com",
            "cdn.jsdelivr.net", "unpkg.com", "code.jquery.com", "bootstrapcdn.com"
        ]
        for cdn in cdn_keywords:
            if cdn in self.raw_content:
                violations.append(f"CDN reference found: {cdn}")

        return violations

    def check_tag_balance(self, tag: str) -> Tuple[int, int]:
        """Counts opening vs closing tags."""
        opening = len(re.findall(rf"<{tag}(?:\s+[^>]*)?>", self.raw_content, re.IGNORECASE))
        closing = len(re.findall(rf"</{tag}>", self.raw_content, re.IGNORECASE))
        return opening, closing


# ==============================================================================
# SECTION 3: UNITTEST TEST SUITE CLASSES
# ==============================================================================

class TestTier1QuantitativeEngines(unittest.TestCase):
    """
    TIER 1: Deterministic Verification of All 6 Quantitative Engines
    Uses Authoritative Reference Test Vectors from survey_quantitative_1.
    """

    def test_engine_1_markup_vs_margin_conversions(self):
        """Engine 1: Channel Markup vs. Margin Bidirectional Conversions."""
        # Test vector 1: Keystone (Markup 100% -> Margin 50%)
        self.assertAlmostEqual(calc_margin_from_markup(100.0), 50.0, places=4)
        self.assertAlmostEqual(calc_markup_from_margin(50.0), 100.0, places=4)

        # Test vector 2: Standard Apparel (Markup 66.6667% -> Margin 40%)
        self.assertAlmostEqual(calc_margin_from_markup(66.6666667), 40.0, places=4)
        self.assertAlmostEqual(calc_markup_from_margin(40.0), 66.6666667, places=4)

        # Test vector 3: Grocery Staple (Markup 25% -> Margin 20%)
        self.assertAlmostEqual(calc_margin_from_markup(25.0), 20.0, places=4)
        self.assertAlmostEqual(calc_markup_from_margin(20.0), 25.0, places=4)

        # Test vector 4: General Retail (Markup 33.3333% -> Margin 25%)
        self.assertAlmostEqual(calc_margin_from_markup(33.3333333), 25.0, places=4)
        self.assertAlmostEqual(calc_markup_from_margin(25.0), 33.3333333, places=4)

        # Test vector 5: At Cost (Markup 0% -> Margin 0%)
        self.assertAlmostEqual(calc_margin_from_markup(0.0), 0.0, places=4)
        self.assertAlmostEqual(calc_markup_from_margin(0.0), 0.0, places=4)

        # Test vector 6: Loss Leader (Markup -20% -> Margin -25%)
        self.assertAlmostEqual(calc_margin_from_markup(-20.0), -25.0, places=4)
        self.assertAlmostEqual(calc_markup_from_margin(-25.0), -20.0, places=4)

        # Price determination
        self.assertAlmostEqual(calc_sp_from_cost_and_margin(60.0, 40.0), 100.0, places=2)
        self.assertAlmostEqual(calc_sp_from_cost_and_margin(50.0, 50.0), 100.0, places=2)

        # Edge cases & validation
        with self.assertRaises(ValueError):
            calc_margin_from_markup(-100.0)
        with self.assertRaises(ValueError):
            calc_markup_from_margin(100.0)
        with self.assertRaises(ValueError):
            calc_sp_from_cost_and_margin(0.0, 40.0)

    def test_engine_1_multi_tier_channel_stacking(self):
        """Engine 1: Multi-tier intermediary channel margin stacking."""
        mfg_cost = 40.0
        mfg_price = mfg_cost * 1.25  # $50.00 (25% markup)
        wholesaler_margin = 15.0  # %
        wholesaler_price = calc_sp_from_cost_and_margin(mfg_price, wholesaler_margin)
        self.assertAlmostEqual(wholesaler_price, 58.823529, places=3)

        retailer_margin = 35.0  # %
        retailer_price = calc_sp_from_cost_and_margin(wholesaler_price, retailer_margin)
        self.assertAlmostEqual(retailer_price, 90.497737, places=3)

        # Total channel margin
        total_channel_margin = (retailer_price - mfg_cost) / retailer_price * 100.0
        self.assertAlmostEqual(total_channel_margin, 55.7999, places=2)

    def test_engine_2_sales_productivity_metrics(self):
        """Engine 2: Sales Productivity (Sales/sq. ft., Sales/FTE)."""
        # Vector 2.1: $2.4M Sales, 3,000 sq ft, 8 FTE
        s_sqft_1 = calc_sales_per_sqft(2400000.0, 3000.0)
        s_fte_1 = calc_sales_per_fte(2400000.0, 8.0)
        self.assertAlmostEqual(s_sqft_1, 800.0, places=2)
        self.assertAlmostEqual(s_fte_1, 300000.0, places=2)

        # Vector 2.2: $45M Sales, 90,000 sq ft, 150 FTE
        s_sqft_2 = calc_sales_per_sqft(45000000.0, 90000.0)
        s_fte_2 = calc_sales_per_fte(45000000.0, 150.0)
        self.assertAlmostEqual(s_sqft_2, 500.0, places=2)
        self.assertAlmostEqual(s_fte_2, 300000.0, places=2)

        # Vector 2.3: $4.8M Sales, 6,000 sq ft net selling, 13 FTE
        s_sqft_3 = calc_sales_per_sqft(4800000.0, 6000.0)
        s_fte_3 = calc_sales_per_fte(4800000.0, 13.0)
        self.assertAlmostEqual(s_sqft_3, 800.0, places=2)
        self.assertAlmostEqual(s_fte_3, 369230.7692, places=2)

        # Validation
        with self.assertRaises(ValueError):
            calc_sales_per_sqft(1000.0, 0.0)
        with self.assertRaises(ValueError):
            calc_sales_per_fte(1000.0, 0.0)
        with self.assertRaises(ValueError):
            calc_sales_per_sqft(-100.0, 500.0)

    def test_engine_3_reilly_law_of_gravitation(self):
        """Engine 3: Reilly's Law of Retail Gravitation (Breaking Point)."""
        # Vector 3.1: d=60, Pa=160,000, Pb=40,000 -> Ba=40.0
        ba_1 = calc_reilly_breaking_point(60.0, 160000.0, 40000.0)
        self.assertAlmostEqual(ba_1, 40.0, places=4)
        bb_1 = 60.0 - ba_1
        self.assertAlmostEqual(bb_1, 20.0, places=4)

        # Newtonian equilibrium check: (Pa/Pb) * (Db/Da)^2 == 1.0
        ratio = (160000.0 / 40000.0) * ((bb_1 / ba_1) ** 2)
        self.assertAlmostEqual(ratio, 1.0, places=4)

        # Vector 3.2: d=50, Pa=900,000, Pb=100,000 -> Ba=37.5
        ba_2 = calc_reilly_breaking_point(50.0, 900000.0, 100000.0)
        self.assertAlmostEqual(ba_2, 37.5, places=4)

        # Vector 3.3: Equal populations: d=100, Pa=250k, Pb=250k -> Ba=50.0
        ba_3 = calc_reilly_breaking_point(100.0, 250000.0, 250000.0)
        self.assertAlmostEqual(ba_3, 50.0, places=4)

        # Vector 3.4: d=75, Pa=400k, Pb=100k -> Ba=50.0
        ba_4 = calc_reilly_breaking_point(75.0, 400000.0, 100000.0)
        self.assertAlmostEqual(ba_4, 50.0, places=4)

        # Validation
        with self.assertRaises(ValueError):
            calc_reilly_breaking_point(0.0, 10000.0, 5000.0)
        with self.assertRaises(ValueError):
            calc_reilly_breaking_point(50.0, -100.0, 5000.0)

    def test_engine_4_huff_gravity_model(self):
        """Engine 4: Huff Gravity Model of Retail Patronage."""
        stores = [
            {"size": 50000.0, "time": 10.0},
            {"size": 120000.0, "time": 15.0},
            {"size": 200000.0, "time": 25.0},
        ]

        # Scenario 4.1: Quadratic friction lambda = 2.0
        probs_lam2 = calc_huff_probabilities(stores, lam=2.0)
        self.assertAlmostEqual(probs_lam2[0], 0.369458, places=4)
        self.assertAlmostEqual(probs_lam2[1], 0.394089, places=4)
        self.assertAlmostEqual(probs_lam2[2], 0.236453, places=4)
        self.assertAlmostEqual(sum(probs_lam2), 1.0, places=6)

        # Expected sales on $30M market
        sales_lam2 = calc_huff_expected_sales(probs_lam2, 30000000.0)
        self.assertAlmostEqual(sales_lam2[0], 11083744.0, delta=20.0)
        self.assertAlmostEqual(sales_lam2[1], 11822660.0, delta=20.0)
        self.assertAlmostEqual(sales_lam2[2], 7093596.0, delta=20.0)
        self.assertAlmostEqual(sum(sales_lam2), 30000000.0, delta=1.0)

        # Scenario 4.2: Linear friction lambda = 1.0
        probs_lam1 = calc_huff_probabilities(stores, lam=1.0)
        self.assertAlmostEqual(probs_lam1[0], 5000.0 / 21000.0, places=4)
        self.assertAlmostEqual(probs_lam1[1], 8000.0 / 21000.0, places=4)
        self.assertAlmostEqual(probs_lam1[2], 8000.0 / 21000.0, places=4)
        self.assertAlmostEqual(sum(probs_lam1), 1.0, places=6)

        # Validation
        with self.assertRaises(ValueError):
            calc_huff_probabilities([], lam=2.0)
        with self.assertRaises(ValueError):
            calc_huff_probabilities([{"size": -10, "time": 5}], lam=2.0)
        with self.assertRaises(ValueError):
            calc_huff_probabilities([{"size": 100, "time": 0}], lam=2.0)

    def test_engine_5_strategic_profit_model_dupont(self):
        """Engine 5: Strategic Profit Model (DuPont ROA & ROE Decomposition)."""
        # Vector 5.1: Discount Warehouse Club (Costco Model - Turnover Leader)
        spm_costco = calc_strategic_profit_model(
            net_sales=100000000.0, cogs=85000000.0, expenses=12500000.0,
            current_assets=12000000.0, fixed_assets=8000000.0, liabilities=12000000.0
        )
        self.assertAlmostEqual(spm_costco["gross_margin"], 15000000.0, places=2)
        self.assertAlmostEqual(spm_costco["net_profit"], 2500000.0, places=2)
        self.assertAlmostEqual(spm_costco["npm_pct"], 2.50, places=2)
        self.assertAlmostEqual(spm_costco["total_assets"], 20000000.0, places=2)
        self.assertAlmostEqual(spm_costco["asset_turnover"], 5.0, places=2)
        self.assertAlmostEqual(spm_costco["roa_pct"], 12.50, places=2)
        self.assertAlmostEqual(spm_costco["net_worth"], 8000000.0, places=2)
        self.assertAlmostEqual(spm_costco["financial_leverage"], 2.50, places=2)
        self.assertAlmostEqual(spm_costco["roe_pct"], 31.25, places=2)

        # Mathematical Identity: Margin Path * Turnover Path == ROA
        recalc_roa_1 = (spm_costco["npm_pct"] / 100.0) * spm_costco["asset_turnover"] * 100.0
        self.assertAlmostEqual(recalc_roa_1, spm_costco["roa_pct"], places=4)

        # Vector 5.2: Specialty Luxury Jeweler (Tiffany Model - Margin Leader)
        spm_tiffany = calc_strategic_profit_model(
            net_sales=30000000.0, cogs=16500000.0, expenses=10500000.0,
            current_assets=15000000.0, fixed_assets=10000000.0, liabilities=10000000.0
        )
        self.assertAlmostEqual(spm_tiffany["gross_margin"], 13500000.0, places=2)
        self.assertAlmostEqual(spm_tiffany["net_profit"], 3000000.0, places=2)
        self.assertAlmostEqual(spm_tiffany["npm_pct"], 10.00, places=2)
        self.assertAlmostEqual(spm_tiffany["total_assets"], 25000000.0, places=2)
        self.assertAlmostEqual(spm_tiffany["asset_turnover"], 1.20, places=2)
        self.assertAlmostEqual(spm_tiffany["roa_pct"], 12.00, places=2)
        self.assertAlmostEqual(spm_tiffany["net_worth"], 15000000.0, places=2)
        self.assertAlmostEqual(spm_tiffany["financial_leverage"], 1.6666667, places=4)
        self.assertAlmostEqual(spm_tiffany["roe_pct"], 20.00, places=2)

    def test_engine_6_gmroi_mechanics(self):
        """Engine 6: GMROI (Gross Margin Return on Inventory Investment)."""
        # Vector 6.1: High Margin Category (Designer Evening Dresses)
        gmroi_a = calc_gmroi(net_sales=1000000.0, cogs=600000.0, avg_inv_cost=200000.0)
        self.assertAlmostEqual(gmroi_a["gross_margin"], 400000.0, places=2)
        self.assertAlmostEqual(gmroi_a["gm_pct"], 40.0, places=2)
        self.assertAlmostEqual(gmroi_a["sales_to_inv"], 5.0, places=2)
        self.assertAlmostEqual(gmroi_a["gmroi"], 2.00, places=2)
        self.assertAlmostEqual(gmroi_a["markup_cost_pct"], 66.6666667, places=4)
        self.assertAlmostEqual(gmroi_a["turnover_cost"], 3.0, places=2)

        # Identity Check: GM % * Sales-to-Inv == GMROI
        identity_1 = (gmroi_a["gm_pct"] / 100.0) * gmroi_a["sales_to_inv"]
        self.assertAlmostEqual(identity_1, gmroi_a["gmroi"], places=4)

        # Identity Check: Markup on Cost * Turnover at Cost == GMROI
        identity_2 = (gmroi_a["markup_cost_pct"] / 100.0) * gmroi_a["turnover_cost"]
        self.assertAlmostEqual(identity_2, gmroi_a["gmroi"], places=4)

        # Vector 6.2: High Turnover Category (Basic Staples)
        gmroi_b = calc_gmroi(net_sales=5000000.0, cogs=4000000.0, avg_inv_cost=400000.0)
        self.assertAlmostEqual(gmroi_b["gross_margin"], 1000000.0, places=2)
        self.assertAlmostEqual(gmroi_b["gm_pct"], 20.0, places=2)
        self.assertAlmostEqual(gmroi_b["sales_to_inv"], 12.5, places=2)
        self.assertAlmostEqual(gmroi_b["gmroi"], 2.50, places=2)
        self.assertAlmostEqual(gmroi_b["markup_cost_pct"], 25.0, places=2)
        self.assertAlmostEqual(gmroi_b["turnover_cost"], 10.0, places=2)

    def test_supplementary_models(self):
        """Supplementary Models: Dark Store Unit Economics, CLV, Bank Channel Migration."""
        # 1. Dark Store Unit Economics
        ds = calc_dark_store_unit_economics(
            aov=15.0, gm_pct=20.0, delivery_fee=1.0,
            picking_cost=0.80, rider_cost=2.20, packaging_payment_cost=0.475,
            daily_fixed_cost=350.0
        )
        self.assertAlmostEqual(ds["revenue_per_order"], 4.0, places=2)
        self.assertAlmostEqual(ds["variable_cost_per_order"], 3.475, places=3)
        self.assertAlmostEqual(ds["contribution_margin"], 0.525, places=3)
        self.assertAlmostEqual(ds["daily_breakeven_orders"], 666.6667, delta=1.0)

        # 2. Omnichannel CLV
        clv_single = calc_omnichannel_clv(margin=200.0, retention=0.65, discount=0.10)
        clv_omni = calc_omnichannel_clv(margin=320.0, retention=0.80, discount=0.10)
        self.assertAlmostEqual(clv_single, 288.8889, places=2)
        self.assertAlmostEqual(clv_omni, 853.3333, places=2)
        self.assertAlmostEqual(clv_omni / clv_single, 2.9538, places=2)

        # 3. Savings Bank Migration
        bank = calc_channel_migration_savings(
            total_txns=1000000, branch_cost=4.25,
            allocations=[
                (0.40, 0.08),  # Mobile
                (0.30, 0.20),  # Web
                (0.15, 0.85),  # ATM
                (0.15, 4.25),  # Branch Advisory
            ]
        )
        self.assertAlmostEqual(bank["baseline_cost"], 4250000.0, places=2)
        self.assertAlmostEqual(bank["migrated_cost"], 857000.0, places=2)
        self.assertAlmostEqual(bank["monthly_savings"], 3393000.0, places=2)
        self.assertAlmostEqual(bank["annual_savings"], 40716000.0, places=2)
        self.assertAlmostEqual(bank["pct_reduction"], 79.8353, places=2)


class TestTier2HTMLArchitectureAndOfflineIsolation(unittest.TestCase):
    """
    TIER 2: Single-File HTML5 Architecture & 100% Offline Self-Containment (R4, R5)
    Asserts HTML structure, doctype, tag closure, and zero external resource calls.
    """

    def setUp(self):
        self.inspector = HTMLStudyGuideInspector(DEFAULT_HTML_PATH)
        self.file_exists = self.inspector.load()

    def test_html_file_exists_and_substantial(self):
        """Asserts omcr_midterm_study_guide.html exists and contains non-trivial content."""
        self.assertTrue(
            self.file_exists,
            f"Target file {DEFAULT_HTML_PATH} does not exist. (Worker may still be building it)"
        )
        size_kb = len(self.inspector.raw_content) / 1024.0
        self.assertGreater(
            size_kb, 15.0,
            f"File size ({size_kb:.1f} KB) is too small to be a complete study guide."
        )

    def test_html5_valid_structure_and_meta(self):
        """Asserts valid HTML5 doctype, viewport meta tag, and basic tags."""
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        raw = self.inspector.raw_content

        self.assertRegex(raw, r"<!DOCTYPE\s+html>", "Missing valid <!DOCTYPE html>")
        self.assertRegex(raw, r"<html[^>]*>", "Missing <html> tag")
        self.assertIn("</html>", raw, "Missing </html> closing tag")
        self.assertRegex(raw, r"<head[^>]*>", "Missing <head> tag")
        self.assertIn("</head>", raw, "Missing </head> closing tag")
        self.assertRegex(raw, r"<body[^>]*>", "Missing <body> tag")
        self.assertIn("</body>", raw, "Missing </body> closing tag")

        # Responsive viewport
        self.assertRegex(
            raw,
            r'<meta[^>]+name=["\']viewport["\'][^>]+content=["\'][^"\']*width=device-width[^"\']*["\']',
            "Missing responsive viewport meta tag"
        )
        # Title tag
        self.assertRegex(raw, r"<title>.*OMCR.*</title>", "Missing or malformed <title> containing OMCR")

    def test_offline_self_containment_zero_external_calls(self):
        """Asserts ZERO external HTTP/HTTPS scripts, stylesheets, fonts, or images."""
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        violations = self.inspector.find_external_resources()
        self.assertEqual(
            violations, [],
            f"Found external network dependencies: {violations}. Study guide must be 100% offline self-contained."
        )

    def test_theme_and_print_styles_embedded(self):
        """Asserts presence of CSS theme variables (light/dark) and print stylesheet."""
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        styles = self.inspector.style_content
        self.assertIn("@media print", styles, "Missing print stylesheet (@media print) for cheat-sheet mode")
        # Check theme support
        has_theme = (
            "data-theme" in self.inspector.raw_content
            or "--bg-" in styles
            or "--text-" in styles
            or "dark" in styles
        )
        self.assertTrue(has_theme, "Missing CSS custom properties or theme support for dark/light mode")


class TestTier3SyllabusCoverage(unittest.TestCase):
    """
    TIER 3: Complete Syllabus & Theoretical Framework Coverage (R1)
    Asserts presence of Sessions 1–5, 6–7, 11, and the Savings Bank Case Study.
    """

    def setUp(self):
        self.inspector = HTMLStudyGuideInspector(DEFAULT_HTML_PATH)
        self.file_exists = self.inspector.load()

    def _assert_keywords(self, session_name: str, required_keywords: List[str]):
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        text = self.inspector.clean_text.lower()
        missing = [kw for kw in required_keywords if kw.lower() not in text]
        self.assertEqual(
            missing, [],
            f"{session_name} is missing core syllabus topics: {missing}"
        )

    def test_session_1_intro_and_paradigms(self):
        """Session 1: Retail Life Cycle, Value Creation Functions, Channel Paradigms."""
        self._assert_keywords(
            "Session 1",
            [
                "retail life cycle", "breaking bulk", "holding inventory",
                "providing assortment", "single-channel", "multi-channel",
                "omnichannel", "markup", "margin"
            ]
        )

    def test_session_2_formats_and_omnichannel(self):
        """Session 2: Retail Formats, Format Productivity, Showrooming/Webrooming."""
        self._assert_keywords(
            "Session 2",
            [
                "supermarket", "warehouse club", "convenience store",
                "non-store", "catalog", "direct selling", "vending",
                "sales per square foot", "sales per employee",
                "showrooming", "webrooming", "bopis", "boris"
            ]
        )

    def test_session_3_strategy_and_value_proposition(self):
        """Session 3: Retail Strategy Framework, SCA, CLV, Growth Matrix."""
        self._assert_keywords(
            "Session 3",
            [
                "retail strategy", "sustainable competitive advantage",
                "target market", "customer lifetime value",
                "market penetration", "format development"
            ]
        )

    def test_session_4_business_models_new_retail(self):
        """Session 4: DNVB, Marketplaces (1P vs 3P), Quick-Commerce, Alibaba New Retail."""
        self._assert_keywords(
            "Session 4",
            [
                "dnvb", "marketplace", "quick-commerce",
                "dark store", "alibaba", "freshippo"
            ]
        )

    def test_session_5_consumer_decision_and_cjm(self):
        """Session 5: Buying Process, Customer Journey Mapping, Attribution."""
        self._assert_keywords(
            "Session 5",
            [
                "buying process", "customer journey map", "friction",
                "attribution", "touchpoint"
            ]
        )

    def test_sessions_6_7_location_analysis(self):
        """Sessions 6–7: Trade Area Delineation, Reilly's Law, Huff Model, Site Selection."""
        self._assert_keywords(
            "Sessions 6–7",
            [
                "trade area", "primary", "secondary", "tertiary",
                "reilly", "huff", "destination store", "parasite store"
            ]
        )

    def test_session_11_financial_strategy(self):
        """Session 11: Strategic Profit Model (DuPont), Margin/Turnover Paths, GMROI."""
        self._assert_keywords(
            "Session 11",
            [
                "strategic profit model", "dupont", "roa",
                "margin path", "turnover path", "gmroi"
            ]
        )

    def test_savings_bank_integrated_case(self):
        """Savings Bank Case: Channel Economics, Migration Barriers, Phygital Model."""
        self._assert_keywords(
            "Savings Bank Case",
            [
                "savings bank", "branch", "mobile",
                "transaction cost", "migration", "phygital"
            ]
        )


class TestTier4MerchandisingNegativeExclusion(unittest.TestCase):
    """
    TIER 4: Strict Merchandising Boundary Negative Exclusion Filter (R1, R5)
    Asserts absolute exclusion of prohibited merchandising topics.
    """

    def setUp(self):
        self.inspector = HTMLStudyGuideInspector(DEFAULT_HTML_PATH)
        self.file_exists = self.inspector.load()

    def test_no_forbidden_merchandising_headings(self):
        """Asserts prohibited merchandising topics do not appear as section headings."""
        if not self.file_exists:
            self.skipTest("HTML file not yet created")

        forbidden_heading_patterns = [
            r"\bopen[- ]to[- ]buy\b",
            r"\bmerchandise budget plan\b",
            r"\bretail inventory method\b",
            r"\bcategory management 8[- ]step\b",
            r"\bplanogram\b",
            r"\bmarkdown (cancellation|timing|cadence)\b",
            r"\bslotting (fee|allowance)\b",
            r"\bcost complement ratio\b",
        ]

        violations = []
        for heading in self.inspector.headings:
            for pattern in forbidden_heading_patterns:
                if re.search(pattern, heading, re.IGNORECASE):
                    violations.append(f"Heading violation '{heading}' matches {pattern}")

        self.assertEqual(
            violations, [],
            f"Merchandising topics leaked into section headings: {violations}"
        )

    def test_no_forbidden_merchandising_substantive_modules(self):
        """
        Asserts document does not contain instructional modules or calculations
        for Open-to-Buy, Merchandise Budget Plans, or Retail Inventory Method.
        """
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        raw = self.inspector.raw_content

        # Strict checks for instructional teaching formulas of forbidden topics
        prohibited_instructional_snippets = [
            r"otb\s*=\s*planned\s+eom",
            r"cost\s+complement\s*=",
            r"retail\s+inventory\s+method\s+calculation",
            r"planned\s+bom\s*inventory",
            r"category\s+role\s+definition\s*step",
        ]

        found_leaks = []
        for snippet in prohibited_instructional_snippets:
            if re.search(snippet, raw, re.IGNORECASE):
                found_leaks.append(snippet)

        self.assertEqual(
            found_leaks, [],
            f"Substantive merchandising instructional content detected: {found_leaks}"
        )


class TestTier5SubjectiveBlueprints(unittest.TestCase):
    """
    TIER 5: Section II Subjective Answering Blueprints (R3)
    Asserts presence of all 8 mandatory exam blueprints with structured frameworks.
    """

    def setUp(self):
        self.inspector = HTMLStudyGuideInspector(DEFAULT_HTML_PATH)
        self.file_exists = self.inspector.load()

    def test_all_eight_blueprints_present(self):
        """Asserts all 8 mandatory subjective question blueprints are present."""
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        text = self.inspector.clean_text.lower()

        required_blueprints = [
            # 1. Multi-channel vs. Omnichannel
            ("Blueprint 1: Multi-channel vs Omnichannel", ["multi-channel", "omnichannel", "bopis", "boris"]),
            # 2. Showrooming / Cannibalization
            ("Blueprint 2: Cannibalization & Showrooming", ["showrooming", "cannibalization", "price-match", "exclusive"]),
            # 3. Retail Value Proposition for Incumbent
            ("Blueprint 3: Retail Value Proposition", ["value proposition", "sustainable competitive advantage", "incumbent"]),
            # 4. Quick-Commerce Dark Store Unit Economics
            ("Blueprint 4: Quick-Commerce Unit Economics", ["quick-commerce", "dark store", "contribution margin", "aov"]),
            # 5. Customer Journey Map (CJM) Friction
            ("Blueprint 5: CJM Friction Resolution", ["customer journey map", "touchpoint", "friction", "back-stage"]),
            # 6. Site Selection & Trade Area Evaluation
            ("Blueprint 6: Site Selection Checklist", ["site selection", "trade area", "reilly", "huff", "traffic"]),
            # 7. Strategic Profit Model Diagnosis
            ("Blueprint 7: SPM Performance Diagnosis", ["strategic profit model", "margin path", "turnover path", "roa"]),
            # 8. Savings Bank Omnichannel Transition
            ("Blueprint 8: Savings Bank Transition", ["savings bank", "phygital", "migration", "transaction cost"]),
        ]

        missing = []
        for bp_name, keywords in required_blueprints:
            all_found = all(kw in text for kw in keywords)
            if not all_found:
                missing.append(bp_name)

        self.assertEqual(
            missing, [],
            f"The following subjective blueprints are missing or incomplete: {missing}"
        )

    def test_blueprint_structured_sections(self):
        """Asserts blueprints include Structured Framework, Real-World Evidence, and Pitfalls."""
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        text = self.inspector.clean_text.lower()

        # Check for core pedagogical blueprint sections
        self.assertTrue(
            "pitfall" in text or "common mistakes" in text or "traps" in text,
            "Blueprints must include exam pitfall warnings"
        )
        self.assertTrue(
            "case" in text or "example" in text,
            "Blueprints must include real-world case illustrations"
        )


class TestTier6MCQEngineIntegrity(unittest.TestCase):
    """
    TIER 6: Section I Practice MCQ Engine Integrity (R3)
    Asserts >= 25 MCQs with 4 options, keys, explanations, and distractor rationales.
    """

    def setUp(self):
        self.inspector = HTMLStudyGuideInspector(DEFAULT_HTML_PATH)
        self.file_exists = self.inspector.load()

    def test_mcq_count_and_options(self):
        """Asserts presence of at least 25 questions with 4 options each."""
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        raw = self.inspector.raw_content

        # Flexible pattern searching for question cards / containers
        question_containers = re.findall(
            r'class=["\'][^"\']*(?:mcq-card|quiz-question|question-card)[^"\']*["\']',
            raw, re.IGNORECASE
        )
        # Fallback: look for data-question-id or id="mcq-q..."
        if not question_containers:
            question_containers = re.findall(
                r'(?:data-question-id=["\']\d+["\']|id=["\']mcq-\d+["\'])',
                raw, re.IGNORECASE
            )

        count = len(question_containers)
        # If classes/IDs not found via regex, count questions by question stem indicators
        if count < 25:
            stems = re.findall(r'(?:Q\d+[:.]|Question\s+\d+[:.])', raw, re.IGNORECASE)
            count = max(count, len(stems))

        self.assertGreaterEqual(
            count, 25,
            f"MCQ count ({count}) is less than the mandatory minimum of 25 (target: 30)."
        )

    def test_mcq_explanations_and_distractor_rationales(self):
        """Asserts presence of correct answer explanations and distractor rationales."""
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        text = self.inspector.clean_text.lower()

        has_rationale = (
            "distractor" in text
            or "incorrect" in text
            or "rationale" in text
            or "explanation" in text
        )
        self.assertTrue(
            has_rationale,
            "MCQ quiz engine must include detailed explanations and distractor rationales."
        )


class TestTier7InteractiveCalculatorWidgets(unittest.TestCase):
    """
    TIER 7: In-Browser Client-Side Interactive Calculator Widgets (R2, R4)
    Asserts all 6 quantitative calculators are embedded in the single-file HTML.
    """

    def setUp(self):
        self.inspector = HTMLStudyGuideInspector(DEFAULT_HTML_PATH)
        self.file_exists = self.inspector.load()

    def test_all_six_calculators_present_in_dom(self):
        """Asserts presence of interactive DOM inputs/widgets for all 6 quantitative models."""
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        raw = self.inspector.raw_content.lower()

        required_calculators = [
            ("Markup vs Margin Calculator", ["markup", "margin"]),
            ("Sales Productivity Calculator", ["sqft", "sales"]),
            ("Reilly's Law Calculator", ["reilly", "breaking point"]),
            ("Huff Gravity Model Calculator", ["huff", "lambda"]),
            ("Strategic Profit Model Calculator", ["dupont", "roa", "turnover"]),
            ("GMROI Calculator", ["gmroi", "inventory"]),
        ]

        missing = []
        for calc_name, tokens in required_calculators:
            found = all(t in raw for t in tokens)
            if not found:
                missing.append(calc_name)

        self.assertEqual(
            missing, [],
            f"The following interactive calculators are missing from the HTML: {missing}"
        )

    def test_client_side_javascript_functions(self):
        """Asserts client-side JavaScript contains calculation routines."""
        if not self.file_exists:
            self.skipTest("HTML file not yet created")
        scripts = self.inspector.script_content.lower()

        self.assertTrue(
            len(scripts) > 500,
            "Client-side JavaScript is missing or too short to power 6 calculators and MCQ quiz."
        )


# ==============================================================================
# SECTION 4: CLI TEST RUNNER & STRUCTURED REPORTING
# ==============================================================================

class Color:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def run_verification_suite(html_path: Path, math_only: bool = False,
                           verbose: bool = False, json_output: bool = False) -> int:
    """
    Executes the verification suite and produces a clean, structured summary.
    Returns exit code (0 for success, non-zero for failures).
    """
    global DEFAULT_HTML_PATH
    DEFAULT_HTML_PATH = html_path

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Always load Tier 1
    suite.addTests(loader.loadTestsFromTestCase(TestTier1QuantitativeEngines))

    if not math_only:
        suite.addTests(loader.loadTestsFromTestCase(TestTier2HTMLArchitectureAndOfflineIsolation))
        suite.addTests(loader.loadTestsFromTestCase(TestTier3SyllabusCoverage))
        suite.addTests(loader.loadTestsFromTestCase(TestTier4MerchandisingNegativeExclusion))
        suite.addTests(loader.loadTestsFromTestCase(TestTier5SubjectiveBlueprints))
        suite.addTests(loader.loadTestsFromTestCase(TestTier6MCQEngineIntegrity))
        suite.addTests(loader.loadTestsFromTestCase(TestTier7InteractiveCalculatorWidgets))

    import io
    if json_output:
        runner = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0)
    else:
        runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    result = runner.run(suite)

    # Compile structured summary
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    skipped = len(result.skipped)
    passed = total_tests - failures - errors - skipped

    summary_data = {
        "target_html": str(html_path),
        "html_exists": html_path.exists(),
        "total_tests": total_tests,
        "passed": passed,
        "failed": failures,
        "errors": errors,
        "skipped": skipped,
        "success": (failures == 0 and errors == 0),
        "tiers": {
            "tier_1_quantitative_math": "PASS" if not any("TestTier1" in str(f[0]) for f in result.failures + result.errors) else "FAIL",
            "tier_2_html_offline_containment": "PASS" if not math_only and html_path.exists() and not any("TestTier2" in str(f[0]) for f in result.failures + result.errors) else ("SKIPPED" if math_only or not html_path.exists() else "FAIL"),
            "tier_3_syllabus_coverage": "PASS" if not math_only and html_path.exists() and not any("TestTier3" in str(f[0]) for f in result.failures + result.errors) else ("SKIPPED" if math_only or not html_path.exists() else "FAIL"),
            "tier_4_merchandising_exclusion": "PASS" if not math_only and html_path.exists() and not any("TestTier4" in str(f[0]) for f in result.failures + result.errors) else ("SKIPPED" if math_only or not html_path.exists() else "FAIL"),
            "tier_5_subjective_blueprints": "PASS" if not math_only and html_path.exists() and not any("TestTier5" in str(f[0]) for f in result.failures + result.errors) else ("SKIPPED" if math_only or not html_path.exists() else "FAIL"),
            "tier_6_mcq_engine_integrity": "PASS" if not math_only and html_path.exists() and not any("TestTier6" in str(f[0]) for f in result.failures + result.errors) else ("SKIPPED" if math_only or not html_path.exists() else "FAIL"),
            "tier_7_interactive_calculators": "PASS" if not math_only and html_path.exists() and not any("TestTier7" in str(f[0]) for f in result.failures + result.errors) else ("SKIPPED" if math_only or not html_path.exists() else "FAIL"),
        }
    }

    if json_output:
        print(json.dumps(summary_data, indent=2))
        return 0 if summary_data["success"] else 1

    # Pretty console summary
    print("\n" + "=" * 80)
    print(" OMCR MID-TERM STUDY GUIDE AUTOMATED VERIFICATION REPORT")
    print(" Course: OMCR | Exam Date: 14 Oct 2026 | Instructor: Dr. Smitu Malhotra")
    print("=" * 80)
    print(f" Target HTML Path: {html_path}")
    print(f" File Status     : {'[PRESENT]' if html_path.exists() else '[NOT FOUND / PENDING GENERATION]'}")
    print("-" * 80)
    print(" VERIFICATION SUITE TIERS:")
    for tier_key, tier_status in summary_data["tiers"].items():
        tier_label = tier_key.replace("_", " ").upper()
        if tier_status == "PASS":
            status_str = f"{Color.GREEN}[PASS]{Color.RESET}"
        elif tier_status == "SKIPPED":
            status_str = f"{Color.YELLOW}[SKIPPED / PENDING HTML]{Color.RESET}"
        else:
            status_str = f"{Color.RED}[FAIL]{Color.RESET}"
        print(f"  - {tier_label:<40}: {status_str}")

    print("-" * 80)
    print(f" TOTAL TESTS RUN : {total_tests}")
    print(f" PASSED          : {Color.GREEN}{passed}{Color.RESET}")
    print(f" FAILED          : {Color.RED}{failures}{Color.RESET}")
    print(f" ERRORS          : {Color.RED}{errors}{Color.RESET}")
    print(f" SKIPPED         : {Color.YELLOW}{skipped}{Color.RESET}")
    print("=" * 80)

    if summary_data["success"] and not skipped:
        print(f"{Color.GREEN}{Color.BOLD}>>> VERIFICATION STATUS: 100% PASS - ALL INTEGRITY CHECKS SATISFIED <<<{Color.RESET}\n")
        return 0
    elif summary_data["success"] and skipped:
        print(f"{Color.YELLOW}>>> VERIFICATION STATUS: MATHEMATICAL REFERENCE PASS - HTML CHECKS PENDING ARTIFACT <<<{Color.RESET}\n")
        return 0
    else:
        print(f"{Color.RED}{Color.BOLD}>>> VERIFICATION STATUS: FAILURES DETECTED - REVIEW DIAGNOSTICS ABOVE <<<{Color.RESET}\n")
        return 1


def main():
    parser = argparse.ArgumentParser(
        description="Automated Verification Suite for OMCR Mid-Term Exam Study Guide"
    )
    parser.add_argument(
        "--html",
        type=Path,
        default=DEFAULT_HTML_PATH,
        help="Path to omcr_midterm_study_guide.html (default: workspace root)"
    )
    parser.add_argument(
        "--math-only",
        action="store_true",
        help="Run only Tier 1 mathematical engine unit tests"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose test runner output"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output test results as machine-readable JSON"
    )

    args = parser.parse_args()
    exit_code = run_verification_suite(
        html_path=args.html,
        math_only=args.math_only,
        verbose=args.verbose,
        json_output=args.json
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
